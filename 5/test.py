#!/usr/bin/python3

import robot

m = robot.RobotMotors()

print("forward")
m.move(50)


print("backward:")
m.move(-50)

print("rotate left:")
m.rotate(50);

print("rotate right:")
m.rotate(-50);
