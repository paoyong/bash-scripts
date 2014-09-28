#!/usr/bin/env python
#Requires internet connection
#Some sample inputs: "ls -l", "echo "Hello world"
#Returns a 'pastebin' link of the output of the input

import subprocess
command = input("Enter your command to be sprunged: ")
subprocess.call(command + " | curl -F 'sprunge=<-' http://sprunge.us", shell=True)
