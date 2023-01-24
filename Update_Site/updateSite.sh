#!/bin/bash

# Run git commit with the -a and -m flags, using the command line argument as the commit message
git commit -a -m "$1"

# Push the committed changes to the remote repository
git push

# Use expect to automate the login process
expect <<- DONE
  # Wait for the login prompt and send the login command
  spawn ssh root@sethbarrett.xyz

  # Wait for the command prompt and send the cd command
  expect "$"
  send "cd /var/www/mysite/\r"

  # Wait for the command prompt and send the git pull command
  expect "$"
  send "git pull\r"

  # Exit remote server
  expect "$"
  send "exit"
  
  # Exit the expect script
  expect eof
DONE