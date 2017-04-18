import threading
import time

class timer(threading.Thread):
	def __init__(self, tLimit):
		threading.Thread.__init__(self)
		self.tLimit = tLimit

	def run(self):
		tInit = time.time()
		while 1:
			tNow = time.time()
			if ((tNow - tInit) >= self.tLimit):
				print "time limit reached"
				print "^C"
				break

#timerThread = timer(5) 
# place timerThread.start() in the main python file
#also from threads import timer
