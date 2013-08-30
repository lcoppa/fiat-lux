""" Set led percentage via PWM pulses
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.
#

import time
from Adafruit_PWM_Servo_Driver import PWM

class LED:
    _pwm = None
    _debug = False

    def __init__(self, address=0x40, freq=60, debug=False):
        # set debug level
        self._debug = debug
        # Initialise the PWM device using the default address
        # from Adafruit: 0x40
        self._pwm = PWM(address, debug)
        # Set frequency in Hz
        self._pwm.setPWMFreq(freq)

    def set_led_level(channel, percent):
        # convert percentage in pulse
        pulse = int((percent/100)*4095)
        # set led level
        self._pwm.setPWM(channel, 0, pulse)
        # confirm
        if _debug
            print("LED on channel " + str(channel) +
                  " set to " + str(percent) + "%")






