import board
import adafruit_ahtx0
from numbers import Number

def c_to_f(c: Number) -> Number:
    return c * 1.8 + 32

class Sensor:
    def __init__(self) -> None:
        self._sensor = adafruit_ahtx0.AHTx0(board.I2C())

    @property
    def humidity(self) -> float:
        """Returns the relative humidity"""
        return self._sensor.relative_humidity

    @property
    def temperature(self) -> float:
        """Returns the temperature in fahrenheit"""
        return c_to_f(self._sensor.temperature)

