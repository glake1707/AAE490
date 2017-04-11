import RPi.GPIO as gpio
import os
import thread
import time

gpioPin = 13
gpio.setmode(gpio.BOARD)
gpio.setup(gpioPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
currentState = gpio.input(gpioPin)
   
    
while(1) :
    time.sleep(0.5)
    currentState = gpio.input(gpioPin)
    if currentState == 1:
        time.sleep(1)
        currentState = gpio.input(gpioPin)
        if currentState == 1:
            gpio.cleanup(gpioPin)
            os.system('sudo shutdown now')
         
