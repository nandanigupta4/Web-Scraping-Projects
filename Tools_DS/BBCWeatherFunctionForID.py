import os
import requests  #to get the web page
import json    #to convert API to json format
from urllib.parse import urlencode
import numpy as np 
import pandas as np
import re  #regular expressions operator


def get_ID(test_city):
    test_city.lower()
    location_url = "https://locator-service.api.bbci.co.uk/locations?" + urlencode({
    "api_key": "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv",
    's': test_city,
   'stack': 'aws',
   'locale': 'en',
   'filter': 'international',
   'place-types': 'settlement,airport,district',
   'order': 'importance',
   'a': 'true',
   'format': 'json'
    })
    result= requests.get(location_url).json()
    id = result['response']['results']['results'][0]['id']
    print(id)
get_ID('Pune')