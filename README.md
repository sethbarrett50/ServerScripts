# ServerScripts
This repository contains a collection of shell and python scripts that automate the process of updating my website, my blog, and the RSS feed. These scripts are designed to make it easy to update my online presence with minimal effort.
## Scripts 
- updateBlog.sh: this script automatically logs into my VPS server after committing changes to my website repository and pulls the updates to the server. A string is passed as a comment to fill in the commit message.
- updateBlog.sh: this script automatically uncomments today's blog title in blog.html, adds the new picture and blog post to my website, uses the updateRSS script to update the blog's RSS feed, commits everything to a separate github repo, and then logs in and pulls the updates on my VPS hosting the website.
- updateRSS.sh: his python script uses the BeautifulSoup4 library (bs4) to parse a HTML document and update the contents of a div with the class "blog" as a new item in an RSS feed.
## Prerequisites
- Python3
- BeautifulSoup4 (bs4)
- Shell
- A VPS with a website hosted on it and access to the server via ssh
- A separate github repository for the website
## Usage
1. Clone this repository to your local machine.
2. Modify the variables in the scripts to match your desired settings.
3. Run the appropriate script for your needs.
## License
This project is licensed under the Unlicense. This means that you are free to use, modify, and distribute the work, even for commercial purposes, without the need to provide attribution. For more information, see the full text of the Unlicense in the License file.



