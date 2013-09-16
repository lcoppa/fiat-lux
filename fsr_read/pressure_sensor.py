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
import sys

NO_PRESSURE = 10000             # count value for zero pressure
TEST_PIN = 0            # pin to read from to check if I can indeed read

class PRESSURE_SENSOR:

    _debug = False
    reading = 0

    def __init__(self, debug=False):
        self._debug = debug
        GPIO.setmode(GPIO.BCM)
        # try reading from hw to generate exception on object creation
        #GPIO.setup(pin, GPIO.OUT)
        #GPIO.output(pin, GPIO.LOW)
        #time.sleep(0.1)

       #GPIO.output(TEST_PIN, GPIO.LOW)
        # don't catch exception here, let it go to the caller

    def test_sensor_ok(self):
        """Do hardware check to see if we can read the sensor
        """
        try:
            GPIO.output(TEST_PIN, GPIO.LOW)
            return True
        except Exception:
            print("Cannot read hardware I/O (not running as root?)")
            return False

    def read_pressure(self, pin):
        """Reads pressure sensor by RC timing
        """
        try:
            # reset the count
            self.reading = 0
            # empty the capacitor
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.01)

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

            if self._debug:
                # go to beginning of line, print the prompt
                sys.stdout.write("\rPressure is: {:<11}".format(
                    str(self.reading) if self.reading < NO_PRESSURE else "no pressure"))
                # stay on this line
                sys.stdout.flush()

            return self.reading

        except Exception:
            if self._debug:
                print("Cannot read hardware I/O (not running as root?)")
            return NO_PRESSURE

    def cleanup(self):
        """Run GPIO library cleanup procedure
        """
        GPIO.cleanup()
