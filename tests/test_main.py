import os

import pytest

from testability import main, logic
from tests.conftest import (CITY_NAMES,
                            WEATHER_DATA,
                            HISTORY,
                            MESSAGE)

"""
Test doubles
"""


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
    return HISTORY.copy()


class WriteHistorySpy:

    def write(self, history):
        self.history = history


def output_mock(message):
    assert message == MESSAGE


"""
Tests
"""


@pytest.mark.quick
def test_take_measurement(sample_measurement):
    measurement = main.take_measurement(
        ip_stub,
        city_stub,
        weather_stub,
        logic.make_measurement
    )
    assert measurement == sample_measurement


@pytest.mark.quick
def test_io(sample_measurement, sample_last_measurement):
    spy = WriteHistorySpy()
    last_measurement = main.io(sample_measurement,
                               history_stub,
                               logic.extract_last_measurement,
                               logic.update_history,
                               spy.write)
    assert len(spy.history) == len(history_stub()) + 1
    assert last_measurement == sample_last_measurement


@pytest.mark.quick
def test_output(sample_measurement, sample_last_measurement):
    main.output(sample_measurement,
                sample_last_measurement,
                logic.form_message,
                output_mock)
