#!/bin/false

#Robot control module

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
 
import time
import atexit

mh = Adafruit_MotorHAT(addr = 0x60)

def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)


class RobotMotors:

	def __init__(self):

		self.hat = mh
		self.left = self.hat.getStepper(513, 1)
		self.right = self.hat.getStepper(513, 2)
		self.left.setSpeed(30)
		self.right.setSpeed(30)
		self.pause = 0.01

	def move(self, distance):
		pause = self.pause
		if distance > 0:
			steps = distance
			self.steps(steps, pause, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD)
		elif distance < 0:
			steps = -distance
			self.steps(steps, pause, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD)

	def rotate(self, angle):
		pause = self.pause
		if angle > 0:
			steps = angle
			self.steps(steps, pause, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD)
		elif angle < 0:
			steps = -angle
			self.steps(steps, pause, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD)

	def steps(self, steps, pause, leftDir, rightDir):

		for i in range(steps):
			self.left.oneStep(leftDir, Adafruit_MotorHAT.DOUBLE)
			self.right.oneStep(rightDir, Adafruit_MotorHAT.DOUBLE)
			time.sleep(pause)



