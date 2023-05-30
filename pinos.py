import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
while True:
    #s
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
    #o
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
    #s
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(2)




