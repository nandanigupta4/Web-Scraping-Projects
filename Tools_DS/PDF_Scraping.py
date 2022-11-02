#PDF Scraping through a given URL
#This tutorial will help us to download all the PDFs in a given URL. In addition to downloading the PDF, this tutorial also helps us in reading a PDF and saving a table from the PDF to a conservative structured format like a CSV.
import os
import requests
import pandas as pd
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#We wil be using tables using the Tabula library
import tabula

#Save the contents from url into folder_location
url = 'https://www.premierleague.com/publications'
folder_location = r'C:\NAND\vscode programmes\Tools_DS\premier_league'
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

#THE CODE
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Part 1: Loop through all PDF links in the page
'''for link in soup.select("a[href$='.pdf']"): #we are looping through all the links which end with a gref tag of .pdf
   #Creating the file name same as the PDF file name, rest is to be ignored
   # for example: https://resources.premierleague.com/premierleague/document/2022/07/18/3fceeddc-01d1-4f99-a01c-247fed27682d/Handbook_2022-23_PL-Youth-Development-Rules.pdf
   #filename = os.path.join(folder_location, link['href'].split('/')[-1]) #splitting the url by '/' and picking the last string, i.e. the PDF name
   with open(filename, 'wb') as f:
    f.write(requests.get(urljoin(url,link['href'])).content)'''

#Part 2: Reading a table from a PDF document and storing it in a csv file
'''combined_pdf = folder_location + "/This-is-PL-Interactive-Combined.pdf"
f=tabula.read_pdf(combined_pdf,  pages='18')
print(f)'''

from tabula import convert_into

convert_into(combined_pdf, folder_location +"/table_output.csv", output_format="csv",pages = 18,area=[[275,504,640,900]])
df=pd.read_csv(folder_location+"/table_output.csv")
print(df)