''' 
(1) Write a python program, that checks your location according to your IP.
	Then checks the current weather at your location and writes the result to a file in a regular text format.

(2)	In that same program, create a list with at least 10 cities,
	And print their current weather in the following format:
	“The weather in <city>, <country>(full country name) is XX degrees.

This Py script get my whther by my current geolocation
 
open weathermap API key : B0f3f7f5f01d058bc63e8c2d7301d805 '''

# IMPORT NECESSARY MODULES
import re
import json
from urllib.request import urlopen

# SET VARIBLES
###  GEO-LOCATION
ipurl = 'http://ipinfo.io/json' 
ipresponse = urlopen(ipurl)
ipdata = json.load(ipresponse)
city = ipdata['city']
country=ipdata['country']

### WEATHER-MAP
wturl = "http://api.openweathermap.org/data/2.5/weather?q="
api = "&APPID=B0f3f7f5f01d058bc63e8c2d7301d805"
wtqueary = wturl+city+api
wtresponse = urlopen(wtqueary)
wtdata = json.load(wtresponse)
temp = wtdata['temp']



print("Your current city is: " + city)
print("QEARY URL: " + qqurl)
print("Temp is" + temp)

