import board, time, rainbowio
from neopixel import NeoPixel  # some boards may need to install this driver

pixel_pin = board.NEOPIXEL
num_pixels = 10

pixels = NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

index = 0

while True:
    index = (index + 1) % 255
    for i in range(num_pixels):
        pixels[i] = rainbowio.colorwheel(((i * 256 // num_pixels) + index) & 255)
    pixels.show()
    time.sleep(0)
