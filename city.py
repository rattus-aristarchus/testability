"""Get user's city based on their IP"""

import requests


def ipinfo(ip: str):
    url = 'https://ipinfo.io/' + ip + '/json'
    response = requests.get(url).json()
    return response["city"]


def geolocationdb(ip: str):
    url =  "https://geolocation-db.com/json/" + \
        ip + \
        "&position=true"
    response = requests.get(url).json()
    return response["city"]
