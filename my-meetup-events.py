# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:55:51 2017

@author: Ting
"""

import meetup.api
import config # Where your key is stored
from datetime import datetime

client = meetup.api.Client()
client.api_key = config.MEETUP_KEY # Access the key from the config file

def myMeetupDates(client):
    
    events = client.GetEvents(rsvp='Yes')
    
    for event in events.results:
        # Turn the timestamp from a string to an integer
        intTime = int(event['time'])
        # Turn the timestamp into seconds rather than milliseconds.
        timeInSeconds = intTime/1000
        # Convert to datetime object
        datetimeObject = datetime.fromtimestamp(timeInSeconds)
        # Format to ISO format
        formattedDate = datetimeObject.strftime('Date: %Y-%m-%d / Time: %H:%M')
    
        print(event['name'])
        print(formattedDate)
        print("\n")
    
    
myMeetupDates(client)