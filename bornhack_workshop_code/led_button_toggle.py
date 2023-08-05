from machine import Pin
from time import sleep_ms

led = Pin(5, Pin.OUT)

btn = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    first = btn.value()
    sleep_ms(100)
    second = btn.value()
    
    if first and not second:
        led.value(not led.value())
        print("butten pressed, toggling LED ", str(led.value()))