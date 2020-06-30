# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:06:09 2020

@author: NAYAN
"""

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sft.json", scope)
client = gspread.authorize(creds)
sheet = client.open("sht").sheet1
insertRow = ["hello", 5, "red", "blue"]
import csv
with open('offers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        sheet.insert_row(row)
numRows = sheet.row_count