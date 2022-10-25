import sys
from datetime import datetime, time
from time import sleep
import schedule
from prometheus_client import start_http_server, Gauge, Enum
from src.outlet import Outlet
from src.sensor import Sensor

ON_TIME = time(7, 00)
OFF_TIME = time(18, 00)

def should_be_on() -> bool:
    return ON_TIME <= datetime.now().time() <= OFF_TIME

def main() -> int:
    with Outlet() as outlet:
        if should_be_on():
            outlet.turn_on()

        sensor = Sensor()
        start_http_server(9100) # port defined by Grafana agent config
        humidity = Gauge('cabinet_humidity', 'Relative humidity')
        temp = Gauge('cabinet_temp_fahrenheit', 'Temperature in F')
        light = Enum('cabinet_light_on', 'If light is on', states=['on', 'off'])

        # Schedule sensor readings
        check_humidity = lambda : humidity.set(sensor.humidity)
        schedule.every().minute.do(check_humidity)
        check_temp = lambda : temp.set(sensor.temperature)
        schedule.every().minute.do(check_temp)
        check_light = lambda : light.state('on' if outlet.is_on else 'off')
        schedule.every().minute.do(check_light)

        # Take initial readings
        check_humidity()
        check_temp()
        check_light()

        # Schedule lights
        schedule.every().day.at(ON_TIME.isoformat()).do(outlet.turn_on)
        schedule.every().day.at(OFF_TIME.isoformat()).do(outlet.turn_off)

        while True:
            schedule.run_pending()
            sleep(1)
    return 0

if __name__ == '__main__':
    sys.exit(main())
