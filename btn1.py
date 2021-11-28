from gpiozero import LED
from time import sleep

red = LED(17)

while 1:
    red.on()
    sleep(1)
    
    red.off()
    sleep(1)