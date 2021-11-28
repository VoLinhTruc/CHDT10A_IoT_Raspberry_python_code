from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while 1:
        led.value =  0
        sleep(0.5)
        
        led.value = 0.5
        sleep(0.5)
        
        led.value = 1
        sleep(1)