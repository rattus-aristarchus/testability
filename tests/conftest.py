import pytest
import dotenv
import datetime

from testability import logic

CITY_NAMES = ["Saint Petersburg", "St Petersburg", "Strel'na"]
NONEXISTENT_CITY = "Not_a_city_name"
DATE = datetime.datetime(2023, 11, 15).date()
TEMP = -3
FEELS = -5
WEATHER_DATA = {"main": {"temp": -3, "feels_like": -5}}
RECORD = {"city": "Saint Petersburg",
          "date": DATE,
          "temp": -3,
          "feels": -5}
HISTORY = [RECORD]
MESSAGE = ("Temperature in Saint Petersburg: -3 °C\n"
           "Feels like -5 °C\n"
           "Last measurement taken on 2023-11-15\n"
           "Difference since then: 0 (feels like 0)")


@pytest.fixture(autouse=True, scope="session")
def load_env():
    dotenv.load_dotenv()


@pytest.fixture(scope="function")
def sample_measurement():
    date = datetime.datetime.now().date()
    return logic.Measurement(CITY_NAMES[0], date, TEMP, FEELS)


@pytest.fixture(scope="function")
def sample_last_measurement():
    return logic.Measurement(CITY_NAMES[0], DATE, TEMP, FEELS)


@pytest.fixture(scope="function")
def sample_message():
    return
