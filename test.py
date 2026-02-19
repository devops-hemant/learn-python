#!/usr/bin/python3

import os
import sys
import time

while True:
    # run brew update command
    if os.system("brew update") == 0:
        print("Upgrading brew")  
        os.system("brew upgrade")
        print("brew upgrade successful")
        break
    else:
        print("brew update failed")
        print("Trying again in 5 seconds")
        time.sleep(5)
