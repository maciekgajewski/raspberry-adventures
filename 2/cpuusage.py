#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pins = [17, 18, 27, 22, 23, 24, 25, 4]

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

def display(usage):
	leds = round(usage * 8)
	#print('usage={}, leds={}'.format(usage, leds))
	for i in range(8):
		pin = pins[i]
		if i < leds:
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)

init()		
runup()

# read stats
prev_idle = None
prev_busy = None
while(True):
	with open('/proc/stat', 'r') as stats:
		line = stats.readline()
		fields = line.split()
		assert fields[0] == 'cpu', 'Unrexpect line read from stats'
		idle = int(fields[4]) + int(fields[5])
		busy = int(fields[1]) + int(fields[2]) + int(fields[3]) + int(fields[6]) + int(fields[7])
		if prev_idle is not None:
			idle_d = idle - prev_idle
			busy_d = busy - prev_busy
			usage = float(busy_d) / (busy_d+idle_d)
			display(usage)
		prev_idle = idle
		prev_busy = busy
	time.sleep(1)

			



