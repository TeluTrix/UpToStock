import sys
import os
import re
import requests
import time
from modules.digitec import checkDigitec

listPath="list.txt"
supportedPath="supported.txt"

supportedOpen = open(supportedPath, 'r+')
supportedSites = supportedOpen.readlines()

def checkSupport(link):

    for supportedSite in supportedSites:
        if supportedSite in link:
            return True
        elif supportedSite not in link:
            return False
        else:
            return None

def sortUrl(link):
    for company in supportedSites:
        if(company == "digitec"):
            return checkDigitec(link)
        else:
            return time.strftime("[%H:%M:%S] ") + "Couldn't figure out the company"






listOpen = open(listPath, 'r+')
urls = listOpen.readlines()
listOpen.close()

supportedCount = 0
unsupportedCount = 0
failToCheckCount = 0
for url in urls:
    supportedBool = checkSupport(url)
    if supportedBool == True:
        supportedCount += 1
    elif supportedBool == False:
        unsupportedCount += 1
    else:
        failToCheckCount += 1

print(time.strftime("[%H:%M:%S] ") + "Loaded " + str(len(urls)) + " urls from list.txt")
print(time.strftime("[%H:%M:%S] ") + str(supportedCount) + " out of " + str(len(urls)) + " are supported")

for url in urls:
    print(sortUrl(url))

