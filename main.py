from typing import Callable

import logic
import persistence
import web


def tell_weather(fetch_ip: Callable[[], str],
                 fetch_city: Callable[[str], str],
                 fetch_weather: Callable[[str], dict],
                 read_measurements: Callable[[], str],
                 write_measurements: Callable[[str], None]):
    """Prints current weather at user's location."""

    ip = fetch_ip()
    city = fetch_city(ip)
    data = fetch_weather(city)
    temp = logic.get_temperature(data)
    temp_feels = logic.get_temperature_feels(data)
    old_measurements = read_measurements()
    date, last_temp, last_feels = logic.get_last_measurement(old_measurements)
    new_measurements = logic.update_measurements(temp, temp_feels, old_measurements)
    write_measurements(new_measurements)
    diff, diff_feels = logic.calc_diff(temp, temp_feels, last_temp, last_feels)
    message = logic.form_message(city, temp, temp_feels, diff, diff_feels, date)
    print(message)


if __name__ == '__main__':
    tell_weather(web.ip_ipify,
                 web.city_ipinfo,
                 web.weather_openweathermap,
                 persistence.read_measurements,
                 persistence.write_measurements)
