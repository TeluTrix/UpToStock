import sys
import os
import re
import requests

listPath="list.txt"
supportedPath="supported.txt"

def checkSupport(link):
    supportedOpen = open(supportedPath, 'r+')
    supportedSites = supportedOpen.readlines()

    for supportedSite in supportedSites:
        if supportedSite in link:
            return True
        elif supportedSite not in link:
            return False
        else:
            return None


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

print("Loaded " + str(len(urls)) + " urls from list.txt")
print(str(supportedCount) + " out of " + str(len(urls)) + " are supported")

