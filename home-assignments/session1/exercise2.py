'''
1.
Write a python program, that checks your location according to your IP.
Then checks the current weather at your location and writes the result to a file in a regular text format.

2. 
In that same program, create a list with at least 10 cities,
And print their current weather in the following format:
“The weather in <city>, <country>(full country name) is XX degrees.
'''
# IMPORT NECESSARY MODULES
import re
import json
from urllib.request import urlopen

# SET VARIBLES
###  GEOLOCATION
ipurl = 'http://ipinfo.io/json' 
ipresponse = urlopen(ipurl)
ipdata = json.load(ipresponse)
city = ipdata['city']
country=ipdata['country']

### WEATHERMAP
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=B0f3f7f5f01d058bc63e8c2d7301d805'


print('Region : {} \nCity  : {}'.format(country,city))

