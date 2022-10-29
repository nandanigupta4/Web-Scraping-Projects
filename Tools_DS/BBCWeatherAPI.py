import os
from urllib import response
import requests  #to get the web page
import json    #to convert API to json format
from urllib.parse import urlencode
import numpy as np 
import pandas as np
from bs4 import BeautifulSoup
from datetime import datetime
import re  #regular expressions operator

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
print(daily_high_values)

daily_low_values = soup.find_all('span', attrs={'class':"wr-day-temperature__low-value"})
print(daily_low_values)