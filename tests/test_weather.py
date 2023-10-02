
import main
import city
import pytest
import ipaddress

IP = "92.100.165.4"
CITY = ["Saint Petersburg", "St Petersburg"]
WRONG_CITY = "Not a city name"


def ip_stub():
    return IP


def city_stub(ip):
    return CITY 


def test_weather():

    main.run(
        ip_stub,
        city_stub,
        main.weather_openweathermap
    )


def test_openweathermap():
    with pytest.raises(KeyError):
        main.weather_openweathermap(WRONG_CITY)


def test_ipinfo():
    assert city.ipinfo(IP) in CITY


def test_geolocationdb():
    assert city.geolocationdb(IP) in CITY


def test_ipify():
    ipaddress.ip_address(main.ip_ipify())
