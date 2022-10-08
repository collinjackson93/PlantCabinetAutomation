import board
from digitalio import DigitalInOut, Direction
from microcontroller import Pin

class Outlet:
    def __enter__(self, pin: Pin = board.D17):
        self._outlet = DigitalInOut(pin)
        self._outlet.direction = Direction.OUTPUT
        self.turn_off()
        return self

    def __exit__(self, *exc) -> bool:
        self.turn_off()
        self._outlet.deinit()
        return False

    @property
    def is_on(self) -> bool:
        return self._outlet.value

    def turn_on(self) -> None:
        self._outlet.value = True

    def turn_off(self) -> None:
        self._outlet.value = False
