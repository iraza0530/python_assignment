## Calculate distance and duration between two places using google distance matrix API.

import requests
import json

 
api_key =''
source = input("Enter origin ...   ")
dest = input("Enter destination ...   ")
 
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
r = requests.get(url + 'origins = ' + source +
                   '&destinations = ' + dest +
                   '&key = ' + api_key)
                    
x = r.json()
 
print(x)
