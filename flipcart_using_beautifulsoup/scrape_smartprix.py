#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:31:10 2021

@author: sangeeth
"""
# Things to improve:
#1. Hard Disk and SSD should be seperated
#2. How to handle situations when feature is not available? 
#3. Basically, we need to sort the data and store it as a laptop feature set
#4. How to take user inputs and sort through data. In other words, writing a filter

#
#from selenium import webdriver
from bs4 import BeautifulSoup
#import pandas as pd
import requests 
import csv

#index=0

#Send request to get data from the url
req = requests.get("https://www.smartprix.com/laptops/price-below_55000/exclude_out_of_stock-stock/8_gb_above-ram/intel-cpu_brand/quad_core-cpu_cores/intel_core_i5-cpu/dell-asus-hp-msi-acer-brand/with-ssd/1_tb_above-hdd?sort=spec_score&asc=0&uq=1")  # URL of the website which you want to scrape
#print(req)
#get the raw content from the url
content = req.content # Get the content
#Parse the downloaded content using soup, Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document
soup = BeautifulSoup(content,'html.parser')
#print(soup.prettify())
desc = soup.find_all('h2')
#print(desc[index])

descriptions = [] # Create a list to store the descriptions
fields = []
fields.append('descriptions')


for i in range(len(desc)):
    descriptions.append(desc[i].text)
#    print(descriptions)
    
#    print("\n\n")
#print(descriptions[0])    
#print(len(descriptions))
    
processor=[] #check with 'intel' or 'AMD'
fields.append('processor')
clock_speed=[] #check with 'Clock Speed'
fields.append('clock Speed')
ram=[] #check with 'RAM'
fields.append('ram')
storage=[]# 'check with 'Hard Disk' and 'SSD'
fields.append('storage')
gpu=[]# Check with 'Graphics Card'
fields.append('GPU')
os=[]# Check with 'OS'
fields.append('os')
inch=[] # check with 'inches'
fields.append('inch')
#warranty=[] # check with 'Warranty'
#fields.append('warranty')
price = []
fields.append('price')
rating = []
fields.append('rating')

checkin = soup.find_all('li',class_='f-laptops')
#print(checkin)
if(checkin):
    for li_tag in soup.find_all('ul', class_='pros'):
        for span_tag in li_tag.find_all('li'):
            pros = span_tag.find('span').text
            if("Intel" in pros or 'AMD' in pros): 
                processor.append(pros)
            elif("GHz" in pros): 
                clock_speed.append(pros)
            elif("RAM" in pros): 
                ram.append(pros)
            elif("Hard Disk" in pros or "SSD" in pros):
                storage.append(pros)
            elif("Graphics Card" in pros or 'Integrated' in pros or 'Radeon' in pros): 
                gpu.append(pros)
            elif("OS" in pros):
                os.append(pros)
            elif("inches" in pros):
                inch.append(pros)
#            elif("Warranty" in pros):
#                warranty.append(pros)
                
    for li_tag in soup.find_all('ul', class_='cons'):
        for span_tag in li_tag.find_all('li'):
            cons = span_tag.find('span').text
#            print(cons)
            if("Graphics Card" in cons or 'Integrated' in cons or 'Radeon' in cons or 'UHD' in cons): 
                gpu.append(cons)
            elif("inches" in cons): 
                inch.append(cons)
            elif("OS" in cons): 
                os.append(cons)
#            elif("Hard Disk" in pros or "SSD" in pros):
#                storage.append(pros)
#            elif("Warranty" in cons): 
#                warranty.append(cons)
            
    
    for div_tag in soup.find_all('div', class_='extra'):
        for span_tag in div_tag.find('span', class_='price'):
            price.append(span_tag)

   
    for div_tag in soup.find_all('div', class_='extra'):
#        print(div_tag)
        for span_tag in div_tag.find('div', class_='rating-price-drop'):
#            print(span_tag.attrs.get("data-value", None))
            if(span_tag.attrs.get("data-value", None)!=None):
                rating.append(span_tag.attrs.get("data-value", None))



#Prepare the data to be written down in a csv file
#Firstly check if all the length of arrays match. If they don't, then raise an error. 
#The only way we can treat this error is by using better keywords for searching parameters
        #or by searching through nested class names

#Create list with x sublists each containing y elements
#print(len(descriptions))

filename = "smartprix.csv"
allLaptopList=[]    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
#    csvwriter.writerows(rows) 
    if(len(descriptions)==len(processor)==len(clock_speed)==len(ram)==len(storage)==len(gpu)==len(os)==len(inch)==len(price)==len(rating)):
        print('Dataset sizes matches well. Now preparing output\n')
    #    for noOfFields in range(0, len(fields)):
        
        for entry in range (0, len(descriptions)):
            eachLaptopList=[]
            eachLaptopList.append(descriptions[entry])
            eachLaptopList.append(processor[entry])
            eachLaptopList.append(clock_speed[entry])
            eachLaptopList.append(ram[entry])
            eachLaptopList.append(storage[entry])
            eachLaptopList.append(gpu[entry])
            eachLaptopList.append(os[entry])
            eachLaptopList.append(inch[entry])
#            eachLaptopList.append(warranty[entry])
            eachLaptopList.append(price[entry])
            eachLaptopList.append(rating[entry])
            allLaptopList.append(eachLaptopList)
        csvwriter.writerows(allLaptopList)
        print("Finished extracting data. Written to file named 'smartprix.csv'")
                
    else:
        print('Dataset size does not match. Failed to write csv output\n')
#        exit()
#
#print(len(descriptions))
#print(len(processor))#
#print(len(clock_speed))#
#print(len(ram))
#print(len(storage))
#print(len(gpu))#
#print(len(os))
#print(len(inch))
##print(len(warranty))
#print(len(price))
#print(len(rating))
##
#for i in range(0,len(descriptions)):
#    print(descriptions[i])
#    print(rating[i])
#    print("\n\n")
#print(rating)s