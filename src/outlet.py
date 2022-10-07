import board
from digitalio import DigitalInOut, Direction
from microcontroller import Pin

class Outlet:
    def __init__(pin: Pin = board.D17) -> None:
        self._outlet = DigitalInOut(pin)
        self._outlet.direction = Direction.OUTPUT
        self._outlet.value = False

    @property
    def is_on(self) -> bool:
        return self._outlet.value

    def turn_on(self) -> None:
        self._outlet.value = True

    def turn_off(self) -> None:
        self._outlet.value = False
