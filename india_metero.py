#this script scrapes weather data from Government Website of Meterological department of India.

import requests
from bs4 import BeautifulSoup
import unicodedata
import re

Daily met data of India in Pdf
met_pdf = "http://www.imd.gov.in/section/nhac/dynamic/allindianew.pdf"

url = 'http://city.imd.gov.in/citywx/menu.php'

url1 = 'http://city.imd.gov.in/citywx/'

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

#find states
#soup.find_all("a", {"href" : "##"})

#Finds cites
cities = soup.find_all("a", {"target" : "mainframe"}

url2 = url1 + soup.find_all("a", {"target" : "mainframe"})[0]['href']


#parameters
soup.find_all('tr', {'height' : '15'})


url3 = 'http://city.imd.gov.in/citywx/city_weather.php?id=43333'

#forcast 15 to 21
# 0 to 5
soup.find_all('tr')[15].find_all("td")[0].text
















