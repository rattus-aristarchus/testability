
import web
import persistence
import logic

import pytest
import ipaddress


CITY = ["Saint Petersburg", "St Petersburg", "Strel'na"]
IP = "92.100.165.4"


def test_weather():
    with pytest.raises(KeyError):
        web.fetch_local_weather("Not a city name")


def test_city():
    assert web.fetch_city(IP) in CITY


def test_ip():
    ip = web.fetch_ip()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        pytest.fail(f"{ip} is not a well-formed IP address")
