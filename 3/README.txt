My GrovePi with ultrasonic ranger arrived.

I've decided not to run the install script provided by the manufacturer, as it seems dodgy as hell: 
Piping random stuff curl'd from the net into root shell? Not on my unix!

I've mamage to install a minimal set of dependencies to ugrade the firmware (1.2.2 -> 1.2.7)
and to run the python module proicied, in python3.

I can now read from the ultrasonic ranger (plugged into socket D4) in Python.
I turns out most of the GPIO pins can be still used, so I will re-connect my GPIO led strip
from the previous adventure, and plug it to the inpuit of the sensor.


