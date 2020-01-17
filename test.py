import requests
import sys

#This is a sample API request
response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())
