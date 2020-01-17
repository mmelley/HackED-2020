import requests
import json
import webbrowser

#This is a sample API request
potd = requests.get("https://api.nasa.gov/planetary/apod", params={'api_key':'Ucbi3Q7hlGh9PulKWimpUVVHrOWyMiXdy5SYeaCN','hd':'true'})

potd_json = potd.json()
for i in potd_json:
    print("%s: %s" % (i, potd_json[i]))

webbrowser.open_new(potd_json['url'])
