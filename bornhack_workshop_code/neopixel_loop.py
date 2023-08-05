from neopixel import NeoPixel
from machine import Pin

n = NeoPixel(Pin(13, Pin.OUT), 12)

for i in range(12):
    n[i] = (255, 0, 0)
    n.write()