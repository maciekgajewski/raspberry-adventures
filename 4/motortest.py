#!/usr/bin/python3
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

motor = mh.getStepper(513, 1)
motor.setSpeed(30)

stepping = Adafruit_MotorHAT.SINGLE

print('backward, 10RPM...')
motor.step(513, Adafruit_MotorHAT.BACKWARD, stepping)

print('forward, 30RPM...')
motor.setSpeed(90)
motor.step(513, Adafruit_MotorHAT.FORWARD, stepping)

print('done')


