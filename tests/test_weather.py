
import main
import pytest
import ipaddress


IP = "92.100.165.4"
CITY = "Saint Petersburg"
WRONG_CITY = "Not a city name"
WEATHER = "Temperature in Saint Petersburg: 15 °C\n" + \
          "Feels like 10 °C"


def ip_stub():
    return IP


def city_stub(ip):
    return CITY 


def weather_stub(city):
    if city == CITY:
        return WEATHER
    else:
        return None


def test_weather():

    weather = main.tell_weather(
        ip_stub,
        city_stub,
        weather_stub,
    )

    assert weather == WEATHER


def test_openweathermap():
    with pytest.raises(KeyError):
        main.weather_openweathermap(WRONG_CITY)


def test_ipinfo():
    ip = IP
    assert main.city_ipinfo(ip) == CITY


def test_ipify():
    ipaddress.ip_address(main.ip_ipify())
