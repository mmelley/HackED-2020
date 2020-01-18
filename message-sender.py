import requests
import numpy
import json
from twilio.rest import Client
message = input("What would you like to send?")
destination = "+17808686226"

def send_message(Message, destination):
    #Sends a text message to specified location
    account_sid = 'ACd2a9214e43319d6acef9351f1ce1f5f6'
    auth_token = 'a737cee82ec01b87cd58a8592c15e99b'
    client = Client(account_sid, auth_token)
    r = requests.get('http://api.open-notify.org/astros.json')
    people = r.json()
    #formulate the message that will be sent
    message = client.messages.create(
        to=destination,
        from_="+17786538284",
        body=Message)
    print(message.sid)

send_message(message, destination)