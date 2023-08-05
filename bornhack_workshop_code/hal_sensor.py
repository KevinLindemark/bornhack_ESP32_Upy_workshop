import esp32
from time import sleep

while 1:
    print(esp32.hall_sensor())
    sleep(0.1)