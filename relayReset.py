import RPi.GPIO as gpio

#set the board to GPIO.BOARD standard gpio config
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
print 'pinout  mode set to GPIO.BOARD'

#channels = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

gpio.setup(8,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.output(8, gpio.HIGH)
gpio.output(11, gpio.HIGH)
print 'active channels set inactive'

gpio.cleanup([8,11])
print 'channels cleaned'
