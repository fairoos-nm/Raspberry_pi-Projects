import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

LED =  18

GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,GPIO.HIGH)
time.sleep(1)

GPIO.output(LED,GPIO.LOW)
time.sleep(1)

GPIO.cleanup()

