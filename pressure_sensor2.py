""" Reads the resistor with RC timing _reading for Raspberry Pi
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

NO_PRESSURE = 10000     # count value for zero pressure
DEFAULT_PIN = 18        # default pin to read from


class GPIODriver:

    # class variable (=static)
    _initialised = False

    def __init__(self):
        pass

    def initialise(self):
        if not _initialised:
            GPIO.setmode(GPIO.BCM)
            _initialised = True

class PressureSensor:

    def __init__(self, pin=DEFAULT_PIN, debug=False):
        self._pin = pin
        self._debug = debug
        self._reading = 0

        # initialise GPIO driver
        driver = GPIODriver()
        driver.initialise()

    def test_sensor_ok(self):
        """Do hardware check to see if we can read the sensor
        """
        try:
            GPIO.output(self._pin, GPIO.LOW)
            return True
        except Exception:
            print('Cannot read hardware I/O (not running as root?)')
            return False

    def read_pressure(self):
        """Reads pressure sensor by RC timing
        """
        try:
            # reset the count
            self._reading = 0
            # empty the capacitor
            GPIO.setup(self._pin, GPIO.OUT)
            GPIO.output(self._pin, GPIO.LOW)
            time.sleep(0.01)

            # prepare to read
            GPIO.setup(self._pin, GPIO.IN)

            # Keep counting until the capacitor fills above a certain level and 
            # brings the input high 
            #
            # Low pressure = high count
            # High pressure = low count
            #
            # This takes about 1 millisecond per loop cycle
            while GPIO.input(self._pin) == GPIO.LOW:
                    self._reading += 1
                    # count until we determine there is just no pressure
                    if self._reading >= NO_PRESSURE:
                        break

            if self._debug:
                # go to beginning of line, print the prompt
                sys.stdout.write('\rSensor pin {0} pressure is: {1:<11}'.format(
                    self._pin,
                    str(self._reading) if self._reading < NO_PRESSURE 
                                      else "no pressure"))
                # stay on this line
                sys.stdout.flush()

            return self._reading

        except Exception:
            if self._debug:
                print('Cannot read sensor on pin {0} '
                      '(not running as root?)'.format(self._pin))
            return NO_PRESSURE

    def cleanup(self):
        """Run GPIO library cleanup procedure
        """
        GPIO.cleanup()
