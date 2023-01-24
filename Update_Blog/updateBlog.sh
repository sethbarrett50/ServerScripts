#!/bin/bash

# Get current day
day=$(date +%d)

# Get current month
month=$(date +%m)

# Get current year
year=$(date +%y)

# Updates RSS feed for daily post
/Users/SEBARRETT/Code/updateRSS.sh ${month}_${day}_20${year}.html

# Changes pwd to site repo directory
cd /Users/SEBARRETT/Code/mysite/

# Add the page containing the new post to the repo
git add /Users/SEBARRETT/Code/mysite/blogposts/${month}_${day}_20${year}.html

# Add the photo for the new post to the repo
git add /Users/SEBARRETT/Code/mysite/blogposts/photos/${month}_${day}_${year}.webp

# Removes last commented section in blog.html
python3 /Users/SEBARRETT/Code/updateBlog.py

# Use site script
/Users/SEBARRETT/Code/updateSite.sh "Added Daily Blogpost"