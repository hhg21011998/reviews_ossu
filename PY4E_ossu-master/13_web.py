import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data.
# Add error checking so your program does not traceback if the country code is not there.
# Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.

# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     print(json.dumps(js, indent=4))
#
#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     alpha2code = js["results"][0]["address_components"][3]["short_name"]
#     print(alpha2code)
# Code: http://www.py4e.com/code3/geojson.py



# Autograder: Extracting Data from XML

# url = input("Enter url: ")
# if url != "http://py4e-data.dr-chuck.net/comments_1456361.xml":
#     url = "http://py4e-data.dr-chuck.net/comments_1456361.xml"
#     print("Url:", url)
# fhand = urllib.request.urlopen(url)
# fxml = ""
# for line in fhand:
#     fxml += line.decode()
#
# tree = ET.fromstring(fxml)
# lst = tree.findall("comments/comment")
# print("Count:", len(lst))
# sum = 0
#
# for item in lst:
#     count = int(item.find("count").text)
#     sum += count
# print(sum)



# Autograder: Extract Data from JSON

# url = input("Enter url: ")
#
# if url != "http://py4e-data.dr-chuck.net/comments_1456362.json":
#     url = "http://py4e-data.dr-chuck.net/comments_1456362.json"
#     print("Url:", url)
#
# fhand = urllib.request.urlopen(url) #return a <class 'http.client.HTTPResponse'>
# # print(type(fhand))
# data = fhand.read().decode() #return a <class 'str'>
# # print(type(data))
# js = json.loads(data) #return a <class 'dict'>
# print(type(js))
# sum = 0
#
# for item in js["comments"]:
#     sum += int(item["count"])
# print(sum)



# Autograder: Using the GeoJSON API

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

key = 42

url = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter a address: ")

param = dict()

param["address"] = address
param["key"] = key

jsonURL = url + urllib.parse.urlencode(param)

data = urllib.request.urlopen(jsonURL, context=ctx)
dataString = data.read().decode()

js = json.loads(dataString)
print(js["results"][0]["place_id"])
