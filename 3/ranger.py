#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import grovepi
import math

pins = [17, 18, 27, 22, 23, 24, 25, 4]
RANGER_SOCKET = 4

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)

def runup():
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(pin, GPIO.LOW)

# Displays value [0, 1]
def display(value):
	leds = round(value * 8)
	#print('usage={}, leds={}'.format(usage, leds))
	for i in range(8):
		pin = pins[i]
		if i < leds:
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)

init()		
runup()

def log_scale(reading):
	max = math.log(515)
	logrange = math.log(reading)
	value = 1 - min(1.0, logrange/max)
	return value

def proximity_scale(reading, max_dist):
	value = 1 - min(1.0, reading/max_dist)
	return value


# Read sensor in a loop, display the value
# Sensor retruns value from 0 (very close) to 515 (very far). It seems to be in cm
while True:
	reading = grovepi.ultrasonicRead(RANGER_SOCKET)
	value = proximity_scale(reading, 30)
	display(value)
	#print('reading={}, value={}'.format(reading, value))
	time.sleep(0.1)
		



