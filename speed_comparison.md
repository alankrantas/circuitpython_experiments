This was a quick test to see how Raspberry Pi Pico performs compared to other similar products in MicroPython/CircuitPython.

Boards:

* WeMos D1 mini (ESP8266/Xtensa LX106)
* Espressif ESP32-Pico-Kit (ESP32/Xtensa LX6, 240 MHz)
* Espressif ESP32-S2 Saola WROVER (ESP32S2/Xtensa LX7, 240 MHz)
* Adafruit Metro M4 Express (ATSAMD51J19A, 120 MHz)
* Raspberry Pi Pico (RP2040, up to 133 MHz)

The codes are the same except using different modules (like math, random, time) in respective firmwares.

Firmwares:

* ESP8266/ESP32: MicroPython v1.13
* ESP32-S2 and Metro M4: CircuitPython 6.1.0
* RPi Pico uses MicroPython v1.13 and CircuitPython 6.2.0 beta

Notes:

* RPi Pico appers to run at 125 MHz in both MicroPython and CircuitPython.
* ESP8266 can be set to 160 MHz in MP. By default ESP32 runs only at 160 MHz in MP. I set it to 240 MHz.
* ESP32 and RPi Pico's processors are dual core. I've tried other ESP32 boards but there's no different to ESP32-Pico.

### Solving 8-Queens problem (using a single Python list with recursion)

Python list - even on microcontrollers - is usually faster compared to bytearray and array (from the array module).

* D1 mini (160 MHz): 2645.56 ms	
* ESP32-Pico-Kit (240 MHz): 2100.727 ms
* RPi Pico (MicroPython): 2284.749 ms
* ESP32-S2 Saola: 3266.36 ms
* Metro M4: 1575.32 ms
* RPi Pico (CircuitPython): 1956.05 ms

### Conway's Game of Life on a 64x32 board (using bytearrays nested in a list), single generation calculation time

This was originally written to display Conway's Game of Life on a 128x64 SSD1306 OLED module. So I have to use bytearray to save memory.

* D1 mini (160 MHz): 1032~1034 ms
* ESP32-Pico-Kitt (240 MHz): 561~564 ms
* RPi Pico (MicroPython): 739~742 ms
* ESP32-S2 Saola: 408~414 ms
* Metro M4: 496~501 ms
* RPi Pico (CircuitPython: 583~584 ms

### SEFR classification training time on IRIS dataset (150 instances x 4 features with 3 labels), using Python lists, garbage collection enabled

Runs list comprehensions and calculates some floating numbers.

* D1 mini (160 MHz): 208.01 ms
* ESP32-Pico-Kitt (240 MHz): 169.769 ms
* RPi Pico (MicroPython): 175.757 ms
* ESP32-S2 Saola (no ulab): 242.554 ms
* Metro M4 (no ulab): 122.803 ms
* RPi Pico (no ulab): 166.992 ms
* ESP32S2 Saola (using ulab): 69.8242 ms
* Metro M4 (using ulab): 45.5322 ms
* RPi Pico (CircuitPython, using ulab): 70.3125 ms

ulab is a simplified Numpy module in CircuitPython, which is not avaliable for SAMD21 boards.

### Conclusion

* CircuitPython usually runs a bit faster than MicroPython.
* RPi Pico performs very, very close to ESP32.
* Metro M4 is usually the fastest.
