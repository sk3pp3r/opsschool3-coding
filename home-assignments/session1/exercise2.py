'''
1.
Write a python program, that checks your location according to your IP.
Then checks the current weather at your location and writes the result to a file in a regular text format.

2. 
In that same program, create a list with at least 10 cities,
And print their current weather in the following format:
“The weather in <city>, <country>(full country name) is XX degrees.
'''
import requests 
from requests import get


location_by_ip_api = get('http://ip-api.com/json').text
geo_list = str(location_by_ip_api)
print(geo_list)

