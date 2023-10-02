"""Get user's city based on their IP"""

import requests
from urllib.request import urlopen
from json import load


def ipinfo(ip):
    ip_address = ip
    url = 'https://ipinfo.io/' + ip_address + '/json'
    response = urlopen(url)
    json = load(response)
    return json["city"]


def geolocationdb(ip):
    response = requests.get(
        "https://geolocation-db.com/json/" + \
        ip + \
        "&position=true"
    ).json()
    return response["city"]
