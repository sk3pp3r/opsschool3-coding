'''
1.
Write a python program, that checks your location according to your IP.
Then checks the current weather at your location and writes the result to a file in a regular text format.

2. 
In that same program, create a list with at least 10 cities,
And print their current weather in the following format:
“The weather in <city>, <country>(full country name) is XX degrees.
'''
# import necessary modules
import re
import json
from urllib.request import urlopen

# set varibles
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

city = data['city']
country=data['country']

print('Region : {} \nCity  : {}'.format(country,city))

