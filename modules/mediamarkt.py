import requests
import time
import re


def checkMediaMarkt(link):
    r = requests.get(link)
    time.sleep(3)
    try:
        if("Leider keine Lieferung möglich" in r.text):
            time.sleep(2)
            productName = re.search('property="og:title" content="(.*)" | MediaMarkt"/><meta data-rh="true"', r.text)
            productPrice = re.search(',"price":(.*),"availability"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Not Available (Only in a few local stores) - " + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
        elif("in stock" in r.text):
            time.sleep(2)
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Available! - " + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
        elif ("preorder" in r.text):
            time.sleep(2)
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Not in stock, available for preorder! - " + productName.group(
                1) + " For: " + productPrice.group(1) + " CHF"
        else:
            time.sleep(2)
            productPrice = re.search('property="product:price:amount" content="(.*)"/><meta property="product:price:currency"', r.text)
            productName = re.search('property="og:title" content="(.*)/><meta property="og:description"', r.text)
            return time.strftime("[%H:%M:%S] ") + "Couldn't get Availability - " + productName.group(1) + " For: " + productPrice.group(1) + " CHF"
    except:
        return time.strftime("[%H:%M:%S] ") + "Unexpected error in program"