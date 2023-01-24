import re

# Open the file for reading
with open("/Users/SEBARRETT/Code/mysite/blog.html", "r") as file:
    # Read the contents of the file into a string
    contents = file.read()

# Use a regular expression to find all occurrences of "<!--"
matches = re.finditer("<!--", contents)

# Get the last match
last_match = None
for match in matches:
    last_match = match

# If a match was found
if last_match:
    # Get the start and end indices of the match
    start, end = last_match.start(), last_match.end()
    end = contents.find("-->", start) + 3 # get the end index of comment
    # Remove the match from the contents
    contents = contents[:start] + contents[start + 4:end - 4] + contents[end:]

# Open the file for writing
with open("/Users/SEBARRETT/Code/mysite/blog.html", "w") as file:
    # Write the modified contents to the file
    file.write(contents)
