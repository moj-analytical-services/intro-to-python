import requests
import json

def street_crime(lat, lon, month, year):
    # Use the police API to download data about crime in a
    # mile radius area for a particular month 
    
    # Long strings can be broken up and placed in brackets
    url = (
        "https://data.police.uk/api/crimes-street/"
        f"all-crime?date={year}-{month}&lat={lat}&lng={lon}"
    )
    resp = requests.get(url)
    # Status code of 200 means the request was ok, otherwise
    # something has gone wrong - most likely that there was no 
    # data for that month
    if resp.status_code == 200:
        # A list of json records
        data = json.loads(resp.text)
    else:
        # An empty list
        data = []
    
    return data