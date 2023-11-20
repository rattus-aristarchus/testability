import logic
import web
import persistence


def run():
    measurement = take_measurement()
    history = persistence.read_history()
    last_measurement = logic.extract_last_measurement(history, measurement.city)
    history = logic.update_history(history, measurement)
    persistence.write_history(history)
    message = logic.form_message(measurement, last_measurement)
    print(message)


def take_measurement():
    """Request data on current weather and generate a measurement object"""
    ip = web.fetch_ip()
    city = web.fetch_city(ip)
    data = web.fetch_local_weather(city)
    return logic.make_measurement(city, data)


if __name__ == '__main__':
    run()
