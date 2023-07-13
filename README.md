# CircuitPython Experiments

# Blinky

```python
import board, digitalio, time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.5)
```

# Pulled-Up Button

```python
import board, digitalio, time

btn = digitalio.DigitalInOut(board.D10)
btn.switch_to_input(pull=digitalio.Pull.UP)

while True:
    print(not btn.value)
    time.sleep(0.1)
```

# Files

* ```neopixel.py```: a demo for NeoPixel LEDs. Requires ```neopixel.mpy``` in the drivers bundle.
* ```audiomixer.py```: a demo of using ```audiomixer``` to play multiple audio files
* ```hd44780.mpy```: driver for I2C LCD1602. Fixed I2C timing and converted from [bablokb/circuitpython-hd44780](https://github.com/bablokb/circuitpython-hd44780).

```python
import busio, board
from hd44780 import HD44780

i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000)
display = HD44780(i2c=i2c, address=0x27)

display.clear()
display.write('Hello', 1)
display.write('World', 2)
```

# Resource Links

* [Firmware download](https://circuitpython.org/downloads)
* [Bootloader (SAMD21/51)](https://github.com/adafruit/uf2-samdx1/releases)
* [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials)
* [CircuitPython Essentials Examples](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/CircuitPython_Essentials)
* [CircuitPython API Reference](https://circuitpython.readthedocs.io/en/latest/docs/index.html)
* [Circuit Playground Express CircuitPython API Reference](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/index.html)
* [Circuit Playground Driver bundle (py/mpy and examples)](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
* [font5x8.bin is here](https://github.com/adafruit/Adafruit_CircuitPython_framebuf/tree/master/examples)
