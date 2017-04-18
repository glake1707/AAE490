import RPi.GPIO as gpio
import time
import math

outChannel1 = 8        #in1 pin on relay board  (active low) 
outChannel2 = 11	#in2 pin on erlay board (active low)
relayRunTime = 16       #total time the relay will run in seconds
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup((outChannel1, outChannel2), gpio.OUT)
gpio.output(outChannel1, gpio.HIGH)     #ensures channel starts off
gpio.output(outChannel2, gpio.HIGH)    #ensures channel2 starts off
 
i = 0
ti = time.time()

while 1:
	if ((i % 5) == 0 and (i != 0)):             #every 10 seconds channel 2 activates for 1 second for noise injection
		gpio.output(outChannel2, gpio.LOW)
		print 'channel 2 activated: noise injected for 1 second, time from start = {} (seconds)'.format (time.time() - ti)

	gpio.output(outChannel1, gpio.HIGH)     #channel one activates once per second, alternating high and low(active low)
	time.sleep(1)
	gpio.output(outChannel2, gpio.HIGH)  #deactivate channel 2
	gpio.output(outChannel1, gpio.LOW)
	print 'channel 1 activated: antenna swap 1 second, time from start = {} (seconds)'.format(time.time() - ti)
	time.sleep(1)
	i = i+1
	tf = time.time()
	if ((tf - ti) > relayRunTime ):
		print('time limit reached {} seconds, cleaning channels and exiting....'.format(relayRunTime))
		break
	
