import logic
import web
import persistence


def run():
    ip = web.fetch_ip()
    city = web.fetch_city(ip)
    data = web.fetch_local_weather(city)
    temp = logic.get_temperature(data)
    temp_feels = logic.get_temperature_feels(data)
    old_measurements = persistence.read_measurements()
    date, last_temp, last_feels = logic.get_last_measurement(old_measurements)
    new_measurements = logic.update_measurements(temp, temp_feels, old_measurements)
    persistence.write_measurements(new_measurements)
    diff, diff_feels = logic.calc_diff(temp, temp_feels, last_temp, last_feels)
    message = logic.form_message(city, temp, temp_feels, diff, diff_feels, date)
    print(message)


if __name__ == '__main__':
    run()
