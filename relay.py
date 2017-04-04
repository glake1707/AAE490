import RPi.GPIO as gpio
import time
import math

outChannel1 = 8        #in1 pin on relay board  (active low) 
outChannel2 = 11	#in2 pin on erlay board (active low)
relayRunTime = 14       #total time the relay will run in seconds
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup((outChannel1, outChannel2), gpio.OUT)
gpio.output(outChannel1, gpio.HIGH)     #ensures channel starts off
gpio.output(outChannel2, gpio.HIGH)    #ensures channel2 starts off
 
i = 0
ti = time.time()
while 1:
	if ((i % 6) == 0 and (i != 0)):             #every 12 seconds channel 2 activates for 1 second for noise injection
		gpio.output(outChannel2, gpio.LOW)

	gpio.output(outChannel1, gpio.HIGH)     #channel one activates once per second, alternating high and low(active low)
	time.sleep(1)
	gpio.output(outChannel2, gpio.HIGH)  #deactivate channel 2
	gpio.output(outChannel1, gpio.LOW)
	time.sleep(1)
	i = i+1
	tf = time.time()
	if (tf - ti) > relayRunTime :
		break
	
