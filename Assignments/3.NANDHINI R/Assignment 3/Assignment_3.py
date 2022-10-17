//python code for blinking LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
while True:
 GPIO.output(2,True)
 time.sleep(2)
 GPIO.output(2,False)
 time.sleep(2)


//Python code for Traffic Lights
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
while True:
 print "RED SIGNAL"
 GPIO.output(2,True)
 time.sleep(2)
 GPIO.output(2,False)
 print "YELLOW SIGNAL"
 GPIO.output(17,True)
 time.sleep(2)
 GPIO.output(17,False)
 print "GREEN SIGNAL"
 print(GPIO.output(4,True))
 time.sleep(2)
 GPIO.output(4,False)