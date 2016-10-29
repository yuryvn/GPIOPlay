try:
	import RPi.GPIO as GPIO
except:
	print "Error importing GPIO"

import time
	
GPIO.setmode(GPIO.BOARD)

Pin=23

GPIO.setup(Pin,GPIO.OUT,initial=GPIO.LOW)

#switch on, off

GPIO.output(Pin,GPIO.HIGH)
time.sleep(3)
GPIO.output(Pin,GPIO.LOW)


GPIO.cleanup()

