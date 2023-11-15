
import datetime

import logic
import web
import persistence


def run():
    measurement = take_measurement()
    history = persistence.read_history()
    last_measurement = logic.get_last_measurement(history)
    history = logic.update_history(history, measurement)
    persistence.write_history(history)
    message = logic.form_message(measurement, last_measurement)
    print(message)


def take_measurement():
    ip = web.fetch_ip()
    city = web.fetch_city(ip)
    data = web.fetch_local_weather(city)
    temp = logic.get_temperature(data)
    temp_feels = logic.get_temperature_feels(data)
    date = datetime.datetime.now().date()
    return logic.Measurement(city, date, temp, temp_feels)


if __name__ == '__main__':
    run()
