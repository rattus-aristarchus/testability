import os
import pytest
import ipaddress

from testability import web
from tests.conftest import CITY_NAMES, NONEXISTENT_CITY


def test_openweathermap():
    response = web.fetch_local_weather(NONEXISTENT_CITY)
    assert response["cod"] == "404"


def test_city():
    assert web.fetch_city(os.getenv("IP")) in CITY_NAMES


def test_ip():
    ip = web.fetch_ip()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        pytest.fail(f"{ip} is not a well-formed IP address")
