import datetime
from dataclasses import dataclass


@dataclass
class Measurement:

    city: str
    date: datetime.date
    temp: int
    feels: int


def get_temperature(weather_data):
    """Extract temperature from weather data"""

    return round(weather_data['main']['temp'])


def get_temperature_feels(weather_data):
    """Extract how temperature feels from weather data"""

    return round(weather_data['main']['feels_like'])


def get_last_measurement(history):
    """Extract last measurements from those stored on the drive"""

    measurement = None
    if history and len(history) > 0:
        measurement = Measurement(city=history[-1]["city"],
                                  date=history[-1]["date"],
                                  temp=history[-1]["temp"],
                                  feels=history[-1]["feels"])
    return measurement


def update_history(history, new_measurement):
    record = {"city": new_measurement.city,
              "date": new_measurement.date,
              "temp": new_measurement.temp,
              "feels": new_measurement.feels}
    history.append(record)
    return history


def form_message(measurement, last_measurement):
    """Return a string telling the weather in a particular city"""

    msg = (f"Temperature in {measurement.city}: {str(measurement.temp)} °C"
           f"\nFeels like {str(measurement.feels)} °C")
    if last_measurement is not None:
        diff = measurement.temp - last_measurement.temp
        diff_feels = measurement.feels - last_measurement.feels
        msg += (f"\nLast measurement taken on {last_measurement.date}"
                f"\nDifference since then: {str(diff)} (feels like {str(diff_feels)})")
    return msg
