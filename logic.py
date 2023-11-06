import datetime


def get_temperature(weather_data):
    """Extract temperature from weather data"""

    return round(weather_data['main']['temp'])


def get_temperature_feels(weather_data):
    """Extract how temperature feels from weather data"""

    return round(weather_data['main']['feels_like'])


def get_last_measurement(measurements):
    """Extract last measurements from those stored on the drive"""

    measure_date = None
    last_temp = None
    last_feels = None
    if measurements:
        measure_date = measurements[-1]["date"]
        last_temp = measurements[-1]["temp"]
        last_feels = measurements[-1]["feels"]
    return measure_date, last_temp, last_feels


def calc_diff(temp, feels, last_temp, last_feels):
    if last_temp is None or last_feels is None:
        return None, None
    else:
        return temp - last_temp, feels - last_feels


def update_measurements(temp, temp_feels, measurements):
    record = {"date": datetime.datetime.now().date(),
              "temp": temp,
              "feels": temp_feels}
    measurements.append(record)
    return measurements


def form_message(city, temp, temp_feels, diff, diff_feels, last_date):
    """Return a string telling the weather in a particular city"""

    msg = (f"Temperature in {city}: {str(temp)} °C"
           f"\nFeels like {str(temp_feels)} °C")
    if (diff is not None and
            diff_feels is not None and
            last_date is not None):
        msg += (f"\nLast measurement taken on {last_date}"
                f"\nDifference since then: {str(diff)} (feels {str(diff_feels)})")
    return msg
