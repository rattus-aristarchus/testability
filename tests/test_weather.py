
import main
import pytest
import ipaddress


def test_weather():
    with pytest.raises(KeyError):
        main.weather("Not a city name")


def test_city():
    ip = "92.100.165.4"
    assert main.get_city(ip) == "Saint Petersburg"


def test_ip():
    ipaddress.ip_address(main.get_ip())