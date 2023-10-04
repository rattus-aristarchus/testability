
import main

import pytest
import ipaddress


CITY = ["Saint Petersburg", "St Petersburg", "Strel'na"]


def test_weather():
    with pytest.raises(KeyError):
        main.fetch_local_weather("Not a city name")


def test_city():
    ip = "92.100.165.4"
    assert main.fetch_city(ip) in CITY


def test_ip():
    ip = main.fetch_ip()
    ipaddress.ip_address(ip)
