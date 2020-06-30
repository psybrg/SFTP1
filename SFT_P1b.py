# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:28:01 2020

@author: NAYAN
"""
import pandas as pd
destinationData = pd.read_csv('IXIGO_Codes - Sheet1.csv')
CityCodes = list(destinationData['Code'])
destinationData.set_index('Code',inplace=True)
print(str(destinationData[['Place']]))

From = input('Departure : ')
while(From not in CityCodes):
    From = input("Please Enter valid City Code for Departure : ")

To = input('Arrival :')
while(To not in CityCodes):
    To = input("Please Enter valid City Code Arrival : ")
    
while(From==To):
    print("Your Departure Loc and Arrival Loc are same")
    val = int(input("Press 1 to Change Departure Loc \nPress 2 to Change Arrival Loc \n"))
    if(val!=1 and val!=2):
        while(val!=1 and val!=2):
            val=int(input("Please Enter valid Number \nPress 1 to Change Departure Loc \nPress 2 to Change Arrival Loc \n"))
    if(val==1):
        From = input("Please Enter City Code for Departure : ")
        while(From not in CityCodes):
            From = input("Please Enter valid City Code for Departure : ")

    else:
        To = input("Please Enter City Code for Arrival : ")
        while(To not in CityCodes):
            To = input("Please Enter valid City Code Arrival : ")

from datetime import datetime

DateOfTravel = input("Enter date of Travel in dd/mm/yyyy format \n")
CheckDate = DateOfTravel.split('/')
Check = True

while(Check):
    try:
        Test = datetime(int(CheckDate[2]),int(CheckDate[1]),int(CheckDate[0]))
        Check = False
    except ValueError:
        DateOfTravel = input("Not a valid Date. \n Enter a valid date of Travel in dd/mm/yyyy format \n")
        CheckDate = DateOfTravel.split('/')




import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
url = 'https://www.ixigo.com/search/result/flight/DEL/BOM/06072020//1/0/0/e?source=Search%20Form'
#url = 'https://www.ixigo.com/search/result/flight/' + destinationData.loc[From,'url_param'] + "/" + destinationData.loc[To,'url_param']+"/"+DateOfTravel+"//1/0/0/e?source=Search%20Form"
#response = requests.get(url)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("D:/nynUTILITIES/Installed/chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'lxml')
'''
content = driver.get(URL).page_source
soup1 = BeautifulSoup(content,features="html.parser")
'''
#print(soup.prettify())
results = soup.find(id='content')
res = results.find_all('div', class_='summary-section')
print(len(res))
'''
for provider in res:
    print(provider, end='\n'*2)

'''
import csv
with open('offers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in res:
        # Each i is a new BeautifulSoup object.
        # It is used to extract information.
        name = i.find('a', class_='flight-name')
        departure = i.find('div', class_='left-wing')
        arrival = i.find('div', class_='right-wing')
        price= i.find('div',class_='price')
        offer= i.find('span',class_='dynot')

        if None in (name, departure, arrival, price):
            continue
        writer.writerow([name.text, departure.text, arrival.text, price.text, offer.text])
        print(name.text)
        print(departure.text)
        print(arrival.text)
        print(price.text)
        print(offer.text)
