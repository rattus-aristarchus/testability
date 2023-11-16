import os
import datetime

import pytest

import logic
import main
from tests.conftest import (CITY_NAMES,
                            WEATHER_DATA,
                            DATE, TEMP,
                            FEELS, HISTORY,
                            MESSAGE)


def ip_stub():
    return os.getenv("IP")


def city_stub(ip):
    return CITY_NAMES[0]


def weather_stub(city):
    if city in CITY_NAMES:
        return WEATHER_DATA
    else:
        return None


def history_stub():
    return HISTORY


def write_history_stub(history):
    pass


def output_mock(message):
    assert message == MESSAGE


def test_take_measurement(sample_measurement):
    measurement = main.take_measurement(
        ip_stub,
        city_stub,
        weather_stub,
        logic.make_measurement
    )
    assert measurement == sample_measurement


def test_io(sample_measurement, sample_last_measurement):
    last_measurement = main.io(sample_measurement,
                               history_stub,
                               logic.extract_last_measurement,
                               logic.update_history,
                               write_history_stub)
    assert last_measurement == sample_last_measurement


def test_output(sample_measurement, sample_last_measurement):
    main.output(sample_measurement,
                sample_last_measurement,
                logic.form_message,
                output_mock)
