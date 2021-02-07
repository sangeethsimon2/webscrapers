#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:16:24 2021

@author: sangeeth
"""

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
fields = []
fields.append('descriptions')


for i in range(len(desc)):
    descriptions.append(desc[i].text)
#    print(descriptions)
#    print("\n\n")
#print(descriptions[index])    
#print(len(descriptions))

checkin = soup.find_all('div',class_='_13oc-S')
if(checkin):
    commonclass = soup.find_all('li' , class_='rgWa7D')
    processor=[]
    fields.append('processor')
    ram=[]
    fields.append('ram')
    os=[]
    fields.append('os')
    storage=[]
    fields.append('storage')
    inch=[]
    fields.append('inch')
    warranty=[]
    fields.append('warranty')
    
    
    for i in range(0,len(commonclass)):
        p=commonclass[i].text # Extracting the text from the tags
#        print(p)
        if("Processor" in p): 
            processor.append(p)
        elif("RAM" in p): 
            ram.append(p)
    # If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well    elif("HDD" in p or "SSD" in p):
        elif("HDD" in p or "SSD" in p):
            storage.append(p)
        elif("Operating" in p):
            os.append(p)
        elif("inch" in p):
            inch.append(p)
        elif("Warranty" in p):
            warranty.append(p)
    price_ = soup.find_all('div',class_='_30jeq3 _1_WHN1') 
    price = []
    fields.append('price')
    for i in range(len(price_)):
        price.append(price_[i].text)
        
    rating = []
    fields.append('rating')
    for everyrow in checkin:
        rating.append(everyrow.find('div',class_='_3LWZlK').text)


#Prepare the data to be written down in a csv file
#Firstly check if all the length of arrays match. If they don't, then raise an error. 
#The only way we can treat this error is by using better keywords for searching parameters
        #or by searching through nested class names

#print(rows[0][0])  
#rows = [[0] *(len(fields)) for i in range(len(descriptions))]
#rows = [[] for i in range(len(descriptions))]
#rows = [(0, 0) for i in range(len(fields)) for j in range(len(descriptions))]
#Create list with x sublists each containing y elements

#print(rows[0][0])

filename = "laptop_search_results.csv"
allLaptopList=[]    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
#    csvwriter.writerows(rows) 
    if(len(descriptions)==len(processor)==len(ram)==len(storage)==len(os)==len(inch)==len(warranty)==len(price)==len(rating)):
        print('Dataset sizes matches well. Now preparing output\n')
    #    for noOfFields in range(0, len(fields)):
        
        for entry in range (0, len(descriptions)):
            eachLaptopList=[]
            eachLaptopList.append(descriptions[entry])
            eachLaptopList.append(processor[entry])
            eachLaptopList.append(ram[entry])
            eachLaptopList.append(storage[entry])
            eachLaptopList.append(os[entry])
            eachLaptopList.append(inch[entry])
            eachLaptopList.append(warranty[entry])
            eachLaptopList.append(price[entry])
            eachLaptopList.append(rating[entry])
            allLaptopList.append(eachLaptopList)
        csvwriter.writerows(allLaptopList)
#        print(list1)
#        print(list2)
#        if(fields[noOfFields]=='descriptions'):
#                rows[noOfEntries][noOfFields].append(descriptions[noOfEntries])
#                rows[:][:].append(descriptions[noOfEntries])
#                 rows[noOfEntries][noOfFields] = descriptions[noOfEntries]
#            elif(fields[noOfFields]=='processor'):
#                rows[noOfEntries][noOfFields].append(processor[noOfEntries])
#            elif(fields[noOfFields]=='ram'):
#                rows[noOfEntries][noOfFields].append(ram[noOfEntries])
#            elif(fields[noOfFields]=='storage'):
#                rows[noOfEntries][noOfFields].append(storage[noOfEntries])
#            elif(fields[noOfFields]=='inch'):
#                rows[noOfEntries][noOfFields].append(inch[noOfEntries])
#            elif(fields[noOfFields]=='warranty'):
#                rows[noOfEntries][noOfFields].append(warranty[noOfEntries])
#            elif(fields[noOfFields]=='price'):
#                rows[noOfEntries][noOfFields].append(price[noOfEntries])
#            elif(fields[noOfFields]=='rating'):
#                rows[noOfEntries][noOfFields].append(rating[noOfEntries])
#                
                
    else:
        print('Dataset size does not match. Failed to write csv output\n')
        exit()


#print(rows)


#df = {'Description':descriptions,'Processor':processors,'RAM':ram,'Operating System':os,'Storage':storage,'Display':inches,'Warranty':warranty,'Price':prices}
#
#print(len(descriptions))
#print(len(processors))#
#print(len(ram))
#print(len(storage))
#print(len(os))
#print(len(inches))
#print(len(warranty))
#print(len(prices))
#print(len(ratings))

#print(descriptions)
#print(processors)

#for index in  range(0,24):
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
