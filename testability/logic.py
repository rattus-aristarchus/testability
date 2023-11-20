import datetime
from dataclasses import dataclass


@dataclass
class Measurement:

    city: str
    date: datetime.date
    temp: int
    feels: int

    def __eq__(self, other):
        if not isinstance(other, Measurement):
            return False
        if (self.city == other.city and
                self.date == other.date and
                self.temp == other.temp and
                self.feels == other.feels):
            return True
        else:
            return False


def make_measurement(city, weather_data):
    temp = round(weather_data['main']['temp'])
    temp_feels = round(weather_data['main']['feels_like'])
    date = datetime.datetime.now().date()
    return Measurement(city, date, temp, temp_feels)


def extract_last_measurement(history, city):
    """Extract last measurements from those stored on the drive"""

    measurement = None
    if history is not None:
        for record in reversed(history):
            if record["city"] == city:
                measurement = Measurement(city=record["city"],
                                          date=record["date"],
                                          temp=record["temp"],
                                          feels=record["feels"])
                break
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
