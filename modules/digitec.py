import requests
import time
import re


def checkDigitec(link):
    r = requests.get(link)
    try:
        if("out of stock" in r.text):
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Not Available - " + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
        elif("in stock" in r.text):
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Available! - " + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
        else:
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Couldn't get Availability - "  + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
    except:
        return time.strftime("[%H:%M:%S] ") + "Unexpected error in program"