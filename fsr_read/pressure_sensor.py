""" Reads the resistor with RC timing reading for Raspberry Pi
Requires GPIO 0.3.1a or later
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.
#

import time
import RPi.GPIO as GPIO

class PRESSURE_SENSOR:

    def __init__(self, debug=False):
        _debug = debug
        GPIO.setmode(GPIO.BCM)

    def read_pressure(pin):
        """Reads pressure sensor by RC timing
        """
        # reset the count
        reading = 0
        # empty the capacitor
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

        # prepare to read
        GPIO.setup(pin, GPIO.IN)

        # Keep counting until the capacitor fills above a certain level and brings the input high
        #
        # Low pressure = high count
        # High pressure = low count
        #
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(pin) == GPIO.LOW):
                reading += 1

        # The sensor is not accurate. As I apply pressure, it goes from high count (8000+)
        # to low (~600), then it goes up again (~2000) at max pressure.
        # For now just assume max pressure is when count in minimum.
        # This will look like pressure is reduced at the end, when it is in fact at its maximum
        #
        # TODO: algorithm to keep track where we are in this U-shaped curve
        return reading

    def cleanup():
        """Run GPIO library cleanup procedure
        """
        GPIO.cleanup()


