import os, sys, re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs4, Tag



def readFile(file_path:str) -> str:
    """
    Read the contents of a file and return its content as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If any other error occurs while reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def readTemplate() -> str:
    """
    Read and return the content of a template file used in a scraping process.

    Returns:
        str: The content of the template file as a string.

    Note:
        This function internally calls `readFile` to read the template file.
    """
    return readFile("./Scrape_Blog/template.html")

def readInput() -> str:
    """
    Read and return the content of the input HTML file for a scraping process.

    Returns:
        str: The content of the input HTML file as a string.

    Raises:
        FileNotFoundError: If the input directory or HTML file does not exist.
        ValueError: If multiple HTML files are found in the input directory.
    """
    inputPath = "./Scrape_Blog/input"
    if not os.path.exists(inputPath) or not os.path.isdir(inputPath):
        raise FileNotFoundError(f"Directory '{inputPath}' does not exist.")
    html_files = [file for file in os.listdir(inputPath) if file.endswith(".html")]
    if len(html_files) == 0:
        raise FileNotFoundError(f"No HTML files found in '{inputPath}'.")
    elif len(html_files) > 1:
        raise ValueError(f"Multiple HTML files found in '{inputPath}'. Please ensure there is only one HTML file.")
    return readFile(os.path.join(inputPath, html_files[0]))

def setDate() -> datetime:
    """
    Set and return a datetime object based on a command-line argument or the current date.

    Returns:
        datetime.datetime: A datetime object representing the specified or current date.

    Raises:
        ValueError: If the command-line argument is not in the 'MM-DD-YYYY' format.

    Note:
        - This function parses a date string provided as a command-line argument in 'MM-DD-YYYY' format.
        - If no argument is provided, it returns the current date.
        - An error is raised for an invalid date format.
    """
    if len(sys.argv) > 1:
        try:
            return datetime.strptime(sys.argv[1], '%m-%d-%Y')
        except ValueError:
            print("Invalid date format. Please use 'MM-DD-YYYY'.")
            return datetime.now()
    else:
        return datetime.now()
    
def createPosts(currDate:datetime) -> None:
    """
    Create daily blog post HTML documents based on input data and templates.

    Args:
        currDate (datetime): The current date for the blog post.

    Raises:
        ValueError: If the input data contains invalid HTML elements.

    Note:
        - This function reads input HTML data, processes it, and creates output HTML documents.
        - It inserts the content from the input data into a template, processes HTML elements,
          and removes specific elements such as 'strong', 'h1', 'code', 'span', and 'button'.
        - Each daily blog post is saved as an HTML file in the 'output' directory.

    TODO:
        - Add next & prev button update
        - Add li, ul & ol update

    """
    inputSoup = bs4(readInput(), 'html.parser')
    template = readTemplate()
    for post in inputSoup.find_all('div', class_='markdown'):
        output = bs4(template[:], 'html.parser')
        # input(post.text)
        results = re.search( r"Title: (.*)", post.p.text, re.MULTILINE)
        if results is None:
            title = post.h1.text
        else:
            title = results.group(1)

        # title
        output.find('div', class_='title').string = title
        
        # date 
        output.find('h4').string = currDate.strftime("%B %d, %Y")
        output.find('h2').string = f'Daily Blog Post: {currDate.strftime("%B %d, %Y")}'
        output.find('title').string = f'Daily Blog Post: {currDate.strftime("%B %d, %Y")}'

        # insert body
        startElement = output.find('div', class_='title')
        prevElement = startElement
        for element in post.find_all():
            if isinstance(element, Tag) and element.name == "strong":
                soup = bs4("", "html.parser")
                new_element = soup.new_tag("b")
                new_element.string = element.text
                element = new_element

            if isinstance(element, Tag) and element.name == "h2":
                soup = bs4("", "html.parser")
                new_element = soup.new_tag("h5")
                new_element.string = element.string
                element = new_element

            if isinstance(element, Tag) and element.name == "pre":
                # input(element)
                code = element.find('code', class_='hljs').get_text()
                # input(code)
                new_element = soup.new_tag('p')
                new_pre = soup.new_tag('pre')
                new_pre.string = code
                new_element.append(new_pre)
                element = new_element

            prevElement.insert_after(element)
            prevElement=element
            # input(startElement)

        for strong_tag in output.find_all('strong'):
            strong_tag.extract()
        for h1 in output.find_all('h1'):
            h1.extract()
        for code in output.find_all('code', class_='hljs'):
            code.extract()
        for span in output.find_all('span'):
            span.extract()
        for span in output.find_all('button', class_='flex'):
            span.extract()

        saveFile(output, currDate)
        currDate = currDate + timedelta(days=1)
        

def saveFile(output:bs4, currDate:datetime):
    """
    Save a BeautifulSoup object to an HTML file with a specific date-based filename.

    Args:
        output (bs4.BeautifulSoup): The BeautifulSoup object to be saved as HTML.
        currDate (datetime.datetime): The date used for generating the filename.

    Note:
        - This function creates a directory named 'output' if it doesn't exist.
        - It saves the content of the BeautifulSoup object to an HTML file with a filename
          based on the provided date.
        - The output file is saved in the 'output' directory.

    """
    output_dir = "./Scrape_Blog/output"
    os.makedirs(output_dir, exist_ok=True)
    filename = currDate.strftime("%m_%d_%Y.html")
    file_path = os.path.join(output_dir, filename)
    try:
        with open(file_path, "w") as file:
            file.write(output.prettify())
        print(f"Output written to {file_path}")
        # input()
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")

        

def main():
    createPosts(setDate())

if __name__ == '__main__':
    main()