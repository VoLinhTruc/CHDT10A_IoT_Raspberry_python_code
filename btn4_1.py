from gpiozero import LED
from gpiozero import Button
from signal import pause

led = LED(17)
button = Button(2)

led.source = button

pause()