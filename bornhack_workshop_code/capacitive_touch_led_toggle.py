from machine import Pin, TouchPad


t = TouchPad(Pin(12))
    
from time import sleep_ms

led = Pin(5, Pin.OUT)

button = Pin(4, Pin.IN, Pin.PULL_UP)

led.value(1)
led_status = 0
touched = True
while 1:
    first = button.value()
    sleep_ms(100)
    second = button.value()
    print(t.read())            # Returns a smaller number when touched
#     if first and not second:
#         print("Button pressed")
#         led.value(not led.value())
    if t.read() < 300 and touched == True:
        led.value(not led.value())
        touched = False
    if t.read() > 300:
        touched = True
        
        
        
    #sleep_ms(200)