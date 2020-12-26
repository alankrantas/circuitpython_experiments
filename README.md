# CircuitPython Experiments

Some experiment codes written in CircuitPython, which is a variation of MicroPython mostly designed for SAMD21/51 and nRF52 microcontrollers. ESP32-S2 is supported since CircuitPython 6.0.0.

# Blinky

```python
import board, digitalio, time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

# Resource Links

* Firmware: https://circuitpython.org/downloads
* Bootloader (SAMD21/51): https://github.com/adafruit/uf2-samdx1/releases
* Essentials: https://learn.adafruit.com/circuitpython-essentials
* API Reference: https://circuitpython.readthedocs.io/en/latest/docs/index.html
* Driver bundle: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
* Where to find font5x8.bin: https://github.com/adafruit/Adafruit_CircuitPython_framebuf/tree/master/examples
