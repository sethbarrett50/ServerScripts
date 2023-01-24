# auto_blog_update

This repository contains a python script and a shell script that will automatically uncomment today's blog title in blog.html, add the new picture and blog post to my website, use the updateRSS script to update the blog's rss feed, commit everything to a separate github repo, and then login and pull the updates on my VPS hosting the website.
## Prerequisites
- Python 3
- BeautifulSoup4 (bs4)
- Shell
- A VPS with a website hosted on it and access to the server via ssh
- A separate github repository for the website
## Usage
1. Modify the START_LINE, HTML_PATH, RSS_PATH, and WEBSITE_REPO variables in the python script to match the desired HTML document, RSS feed, and website repository.
2. Run the shell script: ./updateBlog.sh
## License
This project is licensed under the Unlicense. This means that you are free to use, modify, and distribute the work, even for commercial purposes, without the need to provide attribution. For more information, see the full text of the Unlicense in the License file.



