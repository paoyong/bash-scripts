#!/usr/bin/env python
import subprocess
command = input("Enter your command to be sprunged: ")
subprocess.call(command + " | curl -F 'sprunge=<-' http://sprunge.us", shell=True)
