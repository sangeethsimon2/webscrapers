#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:31:10 2021

@author: sangeeth
"""
#
#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import csv

#index=0

#Send request to get data from the url
req = requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1")  # URL of the website which you want to scrape
#print(req)
#get the raw content from the url
content = req.content # Get the content
#Parse the downloaded content using soup, Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document
soup = BeautifulSoup(content,'html.parser')
#print(soup.prettify())
desc = soup.find_all('div' , class_='_4rR01T')
#print(desc[index])

descriptions = [] # Create a list to store the descriptions
for i in range(len(desc)):
    descriptions.append(desc[i].text)
#    print(descriptions)
#    print("\n\n")
#print(descriptions[index])    
#print(len(descriptions))

commonclass = soup.find_all('li' , class_='rgWa7D')


processors=[]
ram=[]
os=[]
storage=[]
inches=[]
warranty=[]



for i in range(0,len(commonclass)):
    p=commonclass[i].text # Extracting the text from the tags
    if("Core" in p): 
        processors.append(p)
    elif("RAM" in p): 
        ram.append(p)
# If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well    elif("HDD" in p or "SSD" in p):
    elif("HDD" in p or "SSD" in p):
        storage.append(p)
    elif("Operating" in p):
        os.append(p)
    elif("Display" in p):
        inches.append(p)
    elif("Warranty" in p):
        warranty.append(p)


#print(processors[index])
#print(ram[index])
#print(storage[index])
#print(os[index])
#print(inches[index])
#print(warranty[index])
    
price = soup.find_all('div',class_='_30jeq3 _1_WHN1') 
# Extracting price of each laptop from the website
prices = []
for i in range(len(price)):
 prices.append(price[i].text)

#print(prices)    

 
 
checkin = soup.find_all('div',class_='_13oc-S')
print(checkin)
#print(len(checkin))
ratings = []
for everyrow in checkin:
    ratings.append (everyrow.find('div',class_='_3LWZlK').text)
#    print(ratinG)
    
#print(len(ratinG))
#rating = soup.find('div',class_='_3LWZlK') 
#Extracting the ratings of each laptop from the website

#rating = soup.find_all('div',class_='_3LWZlK') 
#
#ratings = []
#for i in range(len(rating)):
#    ratings.append(rating[i].text)

#print(len(ratings))

df = {'Description':descriptions,'Processor':processors,'RAM':ram,'Operating System':os,'Storage':storage,'Display':inches,'Warranty':warranty,'Price':prices}
#
print(len(descriptions))
print(len(processors))#
print(len(ram))
print(len(storage))
print(len(os))
print(len(inches))#
print(len(warranty))
print(len(prices))
print(len(ratings))

#for index in  range(0,1):
#    index=3
#    print(descriptions[index])
#    print(processors[index])
#    print(ram[index])
#    print(storage[index])
#    print(os[index])
#    print(inches[index])
#    print(warranty[index])
#    print(prices[index])
#    print(ratings[index])

#dataset = pd.DataFrame(data = df) 

    
#driver = webdriver.Chrome("/usr/bin/chromedriver")
#
#products=[] #List to store name of the product
#prices=[] #List to store price of the product
#ratings=[] #List to store rating of the product
##driver.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=6ff9e8a3-5729-47ae-b422-1bfb88ffb097&as-searchtext=laptop")
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;uniqBStoreParam1=val1&amp;amp;amp;wid=11.productCard.PMU_V2")
#content = driver.page_source
#soup = BeautifulSoup(content)
#for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#    name=a.find('div', attrs={'class':'_3wU53n'})
#    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#    products.append(name.text)
#    prices.append(price.text)
#    ratings.append(rating.text)