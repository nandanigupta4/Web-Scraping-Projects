
import requests  #to get the web page
import pandas as pd
from bs4 import BeautifulSoup as bs

#Load the webpage
url= "https://www.imdb.com/chart/top/"
result = requests.get(url)
#print(result)

#convert to a beatuiful soup object
soup = bs(result.content)

#Print out the HTML 
contents= soup.prettify()
#print(contents[:100])

#Creating empty list
movie_title = []
movie_year = []
movie_rating = []

#Extract HTML tag contents
imdb_table = soup.find(class_="chart full-width")
movie_titlecolumn = imdb_table.find_all(class_="titleColumn")
movie_ratingscolumn = imdb_table.find_all(class_="ratingColumn imdbRating")

for row in movie_titlecolumn:
    title = row.a.text # tag content extraction
    movie_title.append(title)
#print(movie_title)

for row in movie_titlecolumn:
    year = row.span.text
    movie_year.append(year)
#print(movie_year)

for row in movie_ratingscolumn:
    rating = row.strong.text
    movie_rating.append(rating)
#print(movie_rating)

movie_df = pd.DataFrame({'Movie Title': movie_title, 'Year of Release':movie_year,'IMDb Rating':movie_rating})
print(movie_df.head(30))

#movie_df.to_csv("IMDBTOP_250.csv",index=None)

movie_df.to_excel("IMDB_TOP250.xlsx")