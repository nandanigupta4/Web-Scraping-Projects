import os
from urllib import response
import requests  #to get the web page
import json    #to convert API to json format
from urllib.parse import urlencode
import numpy as np 
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import re  #regular expressions operator
from IPython.display import display 

test_city = 'Varanasi'
location_url= "https://locator-service.api.bbci.co.uk/locations?" + urlencode({
    'api_key':'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
    's': test_city ,
    'stack' : 'aws',
    "locale": 'en',
    'filter': 'international',
    "place-types":"settlement,Cairport,district", 
    "order":"importance",
    "format" :"json"
})

#print(location_url)
result = requests.get(location_url).json()
#print(result)

id = result['response']['locations'][0]['id']
#print(id)
url = "https://www.bbc.com/weather/" + id

response = requests.get(url) #to get the html content of the webpage

soup= BeautifulSoup(response.content,'html.parser') #goes through the webpage line by line and extracts the meaniningful info
#Now we have to give the extract block numbers where your specific content resides to the BS to parse it

daily_high_values = soup.find_all('span', attrs={'class':"wr-day-temperature__high-value"})
#print(daily_high_values)

daily_low_values = soup.find_all('span', attrs={'class':"wr-day-temperature__low-value"})
#print(daily_low_values)

daily_summary = soup.find('div', attrs= {'class': "wr-day-summary"})
#print(daily_summary)

#print(daily_summary.text)
#print(daily_high_values[0].text.strip()) # 0th entry ofthe 14 entry list, find the test of that tag, remove the spaces using strip

daily_high_values_list = [daily_high_values[i].text.strip().split()[0] for i in range(len(daily_high_values))]
#print(daily_high_values_list)
daily_low_values_list = [daily_low_values[i].text.strip().split()[0] for i in range(len(daily_low_values))]
#print(daily_low_values_list)
daily_summary_list= re.findall('[a-zA-Z][^A-Z]*',daily_summary.text) #split the string on uppercase
#print(daily_summary_list)

datelist= pd.date_range(datetime.today(), periods=len(daily_high_values)).tolist()
#print(datelist)
datelist = [datelist[i].date().strftime('%y-%m-%d') for i in range(len(datelist))]
#print(datelist)

zipped = zip(datelist, daily_high_values_list, daily_low_values_list,daily_summary)
df= pd.DataFrame(list(zipped), columns=['Date', 'High','Low','Summary'])
#display(df)

#remove the 'degree' character
df.High = df.High.replace('\°','',regex=True).astype(float)
df.Low = df.Low.replace('\°','', regex = True).astype(float)
#display(df)
location = soup.find('h1', attrs={'id':'wr-location-name-id'})
print(location.text.split())

#create a recording
filename_csv = location.text.split()[0]+ '.csv'
df.to_csv(filename_csv,index=None)

filename_xlsx = location.text.split()[0]+ '.xlsx'
df.to_excel(filename_xlsx)