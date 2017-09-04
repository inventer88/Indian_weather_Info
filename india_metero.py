#this script scrapes weather data from Government Website of Meterological department of India.

import requests
from bs4 import BeautifulSoup
import unicodedata
import re
#import sqlite3
import json

#conn = sqlite3.connect('/media/my_book1/data_db/imd_weather.db')

#c = conn.cursor()

imd_tdwthr = {}

def tableCreate():
        c.execute("CREATE TABLE imd_weather(id INTEGER PRIMARY KEY, place TEXT, name TEXT, magneturi TEXT, type TEXT, size INT, seeds INT, leeches INT )")


#Daily met data of India in Pdf
met_pdf = "http://www.imd.gov.in/section/nhac/dynamic/allindianew.pdf"

url = 'http://city.imd.gov.in/citywx/menu.php'

url1 = 'http://city.imd.gov.in/citywx/'

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

#find states
#soup.find_all("a", {"href" : "##"})

#Finds cites
#cities = soup.find_all("a", {"target" : "mainframe"})
for city in soup.find_all("a", {"target" : "mainframe"}):
	print city.text #city name
	url2 = url1 + city['href'] #url2 generated for city weather page 
	r1 = requests.get(url2)
	soup1 = BeautifulSoup(r1.content, "lxml")
	
	#'\n\nMaximum Temp(oC) (Recorded. on 03/09/17)\n\n31.5\n'
	try:
		temp = soup1.find_all('tr', {'height' : '15'})[0].text
	except:
		print "Data not uploaded"
		continue
	#extract digits from string using re module
	try:
		max_temp = float(re.findall('\d+', temp)[3]) + float(re.findall('\d+', temp)[4])/10
	except:
		max_temp = 420
		print temp
	
	#Departure from Normal(oC)
	temp = soup1.find_all('tr', {'height' : '15'})[1].text
	#extract digits from string using re module
	try:
		dept_fnorm = float(re.findall('\d+', temp)[0])
	except:
		dept_fnorm = 420
		print temp
	
	#u'\n\nMinimum Temp (oC) (Recorded. on 03/09/17)\n\n24.8\n'
	temp = soup1.find_all('tr', {'height' : '15'})[2].text
	#extract digits from string using re module
	try:
		min_temp = float(re.findall('\d+', temp)[3]) + float(re.findall('\d+', temp)[4])/10
	except:
		min_temp = 420
		print temp
	
	#u'\n\nDeparture from Normal(oC)\n\n2\n'
	temp = soup1.find_all('tr', {'height' : '15'})[3].text
	#extract digits from string using re module
	try:
		dept_fnorm1 = float(re.findall('\d+', temp)[0])
	except:
		dept_fnorm1 = 420
		print temp
	
	#u'\n\n24 Hours Rainfall (mm) (Recorded from 0830 hrs IST of yesterday to 0830 hrs IST of today)\n\nNIL\n'
	temp = soup1.find_all('tr', {'height' : '15'})[4].text
	#extract digits from string using re module
	try:
		rain_mm = float(re.findall('\d+', temp)[3]) + float(re.findall('\d+', temp)[4])/10
	except:
		rain_mm = 0
		
	#u'\n\nRelative Humidity at 0830 hrs (%)\n\n78\n'
	temp = soup1.find_all('tr', {'height' : '15'})[5].text
	#extract digits from string using re module
	try:
		rhumid_mr = float(re.findall('\d+', temp)[1])
	except:
		rhumid_mr = 420
		print temp
	
	#u'\n\nRelative Humidity at 1730 hrs (%) (Recorded. on 03/09/17)\n\n89\n'
	temp = soup1.find_all('tr', {'height' : '15'})[6].text
	#extract digits from string using re module
	try:
		rhumid_ev = float(re.findall('\d+', temp)[4])
	except:
		rhumid_ev = 420
		print temp
	
	#u'\n\nTodays Sunset (IST)\n\n17-28\n'
	temp = soup1.find_all('tr', {'height' : '15'})[7].text
	#extract digits from string using re module
	try:
		tdy_set = int(re.findall('\d+', temp)[0])*100 + int(re.findall('\d+', temp)[1])
	except:
		tdy_set = 420
		print temp
	
	#u'\n\nTodays Sunset (IST)\n\n17-28\n'
	temp = soup1.find_all('tr', {'height' : '15'})[8].text
	#extract digits from string using re module 
	try:
		tmw_rise = int(re.findall('\d+', temp)[0])*100 + int(re.findall('\d+', temp)[1])
	except:
		tmw_rise = 420
		print temp
	
	#u'\n\nTodays Sunset (IST)\n\n17-28\n'
	temp = soup1.find_all('tr', {'height' : '15'})[9].text
	#extract digits from string using re module 
	try:
		moon_set = int(re.findall('\d+', temp)[0])*100 + int(re.findall('\d+', temp)[1])
	except:
		moon_set = 420
		print temp
	
	#u'\n\nTodays Sunset (IST)\n\n17-28\n'
	temp = soup1.find_all('tr', {'height' : '15'})[10].text
	#extract digits from string using re module
	try:
		moon_rise = int(re.findall('\d+', temp)[0])*100 + int(re.findall('\d+', temp)[1])
	except:
		moon_rise = 420
		print temp
	
	#7 day forecasts
	min_ftemp = []
	max_ftemp = []
	wth_ft = []
	
	for i in range(15,22):
		#min_temp
		temp = soup1.find_all('tr')[15].find_all("td")[1].text
		try:
			min_ftemp.append( float(re.findall('\d+', temp)[0]) + float(re.findall('\d+', temp)[1])/10 )
		except:
			min_ftemp.append(420)
		
		#max_temp
		temp = soup1.find_all('tr')[15].find_all("td")[2].text
		try:
			max_ftemp.append( float(re.findall('\d+', temp)[0]) + float(re.findall('\d+', temp)[1])/10 )
		except:
			max_ftemp.append(420)
		
		#weather
		temp = soup1.find_all('tr')[15].find_all("td")[4].text
		try:
			wth_ft.append( re.sub("\n", "", re.sub(' +',' ',temp)) )
		except:
			wth_ft.append("NA")
	
	imd_tdwthr[city.text] = { 'max_temp': max_temp, 'dept_fnorm': dept_fnorm, 'min_temp': min_temp, \
	"dept_fnorm1": dept_fnorm1, 'rain_mm': rain_mm, 'rhumid_mr': rhumid_mr, 'rhumid_ev': rhumid_ev, \
	'tdy_set': tdy_set, 'tmw_rise': tmw_rise, 'moon_set': moon_set, 'moon_rise': moon_rise, 'min_ftemp0': min_ftemp[0], \
	'max_ftemp0': max_ftemp[0], 'wth_ft0': wth_ft[0], 'min_ftemp1': min_ftemp[1], 'max_ftemp1': max_ftemp[1], \
	'wth_ft1': wth_ft[1], 'min_ftemp2': min_ftemp[2], 'max_ftemp2': max_ftemp[2], 'wth_ft2': wth_ft[2], \
	'min_ftemp3': min_ftemp[3], 'max_ftemp3': max_ftemp[3], 'wth_ft3': wth_ft[3], 'min_ftemp4': min_ftemp[4], \
	'max_ftemp4': max_ftemp[4], 'wth_ft4': wth_ft[4], 'min_ftemp5': min_ftemp[5], 'max_ftemp5': max_ftemp[5], \
	'wth_ft5': wth_ft[5], 'min_ftemp6': min_ftemp[6], 'max_ftemp6': max_ftemp[6], 'wth_ft6': wth_ft[6] }

fname = '/media/my_book/pyth_tut/IMDweather/imd_weather'
imd_tdwthr1 = json.dumps(imd_tdwthr)
with open(fname, "w") as f:
	f.write(imd_tdwthr1)

















