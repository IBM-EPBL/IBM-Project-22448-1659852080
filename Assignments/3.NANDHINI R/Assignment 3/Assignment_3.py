import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)
#Traffic Light
from gpiozero import Button, TrafficLights, Buzzer
from time import sleep
buzzer = Buzzer(15)
button = Button(21)
lights = TrafficLights(25, 8, 7)
#Button 21
#Red LED 25
#Yellow LED 08
#Green LED 07
#Buzzer 15
while True:
  button.wait_for_press()
  buzzer.on()
  light.green.on()
  sleep(1)
  lights.amber.on()
  sleep(1)
  lights.red.on()
  sleep(1)
  lights.off()
  buzzer.off()