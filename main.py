import sys
from datetime import datetime, time
from time import sleep
import schedule
from src.outlet import Outlet

ON_TIME = time(7, 00)
OFF_TIME = time(18, 00)

def should_be_on() -> bool:
    return ON_TIME <= datetime.now().time() <= OFF_TIME

def main() -> int:
    with Outlet() as outlet:
        if should_be_on():
            outlet.turn_on()

        schedule.every().day.at(ON_TIME.isoformat()).do(outlet.turn_on)
        schedule.every().day.at(OFF_TIME.isoformat()).do(outlet.turn_off)
        while True:
            schedule.run_pending()
            sleep(1)
    return 0

if __name__ == '__main__':
    sys.exit(main())
