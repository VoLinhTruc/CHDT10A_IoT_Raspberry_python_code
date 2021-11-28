from gpiozero import Button

button = Button(2)

while 1:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")