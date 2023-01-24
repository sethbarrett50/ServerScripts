# This takes the name of a html doc for a blog posts
# Then adds its contents to the rss file
import sys
import re
import datetime
from bs4 import BeautifulSoup as bs4

# Takes the html document, uses bs4 to get div element with class blog


def getBlogContents() -> tuple[str]:
    with open(f'/Users/SEBARRETT/Code/mysite/blogposts/{sys.argv[1]}', 'r') as f:
        soup = bs4(f.read(), 'html.parser')
    title = soup.find('div', class_='title').text
    contents = re.sub('\n', '', soup.find('div', class_='blog').prettify())
    return (title, contents)


# Adds blog contents to top of channel as a new item
def addToRss(bc: str) -> None:
    RSS_PATH = "/Users/SEBARRETT/Code/mysite/blogposts/rss.xml"
    with open(RSS_PATH, 'r') as rss_file:
        rss_xml = rss_file.read()
    START_LINE = '<atom:link href="https://sethbarrett.xyz/rss.xml" rel="self" type="application/rss+xml"/>'
    channel_start_index = rss_xml.index(START_LINE)
    now = datetime.datetime.now()
    rss_xml = (rss_xml[:channel_start_index+len(START_LINE)] +
               f'\n  <item>\n    <title>{bc[0]}</title>\n\t<link>https://sethbarrett.xyz/blogposts/{sys.argv[1]}</link>\n\t<pubDate>{now.strftime("%a, %d %b %Y %H:%M:%S %z")}+400</pubDate>\n\t<guid>https://sethbarrett.xyz/blogposts/{sys.argv[1]}/</guid>\n\t<description>{bc[1]}</description>\n  </item>' +
               rss_xml[channel_start_index+len(START_LINE):])
    with open(RSS_PATH, 'w') as rss_file:
        rss_file.write(rss_xml)


def main() -> None:
    blogContents = getBlogContents()
    addToRss(blogContents)


if __name__ == "__main__":
    main()
