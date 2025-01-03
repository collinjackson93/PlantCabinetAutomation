# PlantCabinetAutomation
RaspberryPi automation for a greenhouse cabinet with an [AHT20 temperature/humidity sensor](https://www.adafruit.com/product/5181) and growing lights controlled via an [IOT relay](https://www.adafruit.com/product/2935)

## Set Up
* Install CircuitPython/Blinka [link](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#update-your-pi-and-python-2993452)
* Install this python module
* Connect the humidity sensor to the I2C pins and the IOT relay to a GPIO (pin 17 by default)
* Install Grafana Alloy [link](https://grafana.com/docs/alloy/latest/set-up/install/linux/) and configure using example config file
* Install example systemd service
* Install nginx
* Configure nginx for flask server [link](https://flask.palletsprojects.com/en/2.2.x/deploying/nginx/)
