import os
import pytest
import ipaddress
import allure

from testability import web
from tests.conftest import CITY_NAMES, NONEXISTENT_CITY


@allure.tag("slow")
@pytest.mark.slow
def test_openweathermap():
    response = web.weather_openweathermap(NONEXISTENT_CITY)
    assert response["cod"] == "404"


@allure.tag("slow")
@pytest.mark.slow
def test_city():
    assert web.city_ipinfo(os.getenv("IP")) in CITY_NAMES


@allure.tag("slow")
@pytest.mark.slow
def test_ip():
    ip = web.ip_ipify()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        pytest.fail(f"{ip} is not a well-formed IP address")
