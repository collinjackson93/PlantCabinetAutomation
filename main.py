import sys
from datetime import datetime, time
from time import sleep
from src.outlet import Outlet

ON_TIME = time(7, 00)
OFF_TIME = time(18, 00)

def main() -> int:
    with Outlet() as outlet:
        while True:
            CUR_TIME = datetime.now().time()
            if (ON_TIME <= CUR_TIME <= OFF_TIME) and not outlet.is_on:
                outlet.turn_on()
            elif (CUR_TIME > OFF_TIME or CUR_TIME < ON_TIME) and outlet.is_on:
                outlet.turn_off()
            sleep(30)
    return 0

if __name__ == '__main__':
    sys.exit(main())
