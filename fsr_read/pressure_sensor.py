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

NO_PRESSURE = 10000             # count value for zero pressure

class PRESSURE_SENSOR:

    _debug = False
    reading = 0

    def __init__(self, debug=False):
        self._debug = debug
        GPIO.setmode(GPIO.BCM)

    def read_pressure(self, pin):
        """Reads pressure sensor by RC timing
        """
        # reset the count
        self.reading = 0
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
                self.reading += 1
                # count until we determine there is just no pressure
                if self.reading >= NO_PRESSURE:
                    break

        # The sensor is not accurate. As I apply pressure, it goes from high count (8000+)
        # to low (~600), then it goes up again (~2000) at max pressure.
        # For now just assume max pressure is when count in minimum.
        # This will look like pressure is reduced at the end, when it is in fact at its maximum
        #
        # TODO: algorithm to keep track where we are in this U-shaped curve
        if self._debug:
            print('Pressure is: ' + str(self.reading))
        return self.reading

    def cleanup(self):
        """Run GPIO library cleanup procedure
        """
        GPIO.cleanup()


