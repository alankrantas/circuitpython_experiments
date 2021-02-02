# CircuitPython Experiments

Some experiment codes written in CircuitPython, which is a variation of MicroPython mostly designed for SAMD21/51 and nRF52 microcontrollers. ESP32-S2 is supported since CircuitPython 6.0.0.

# Blinky

```python
import board, digitalio, time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.5)
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
