""" Set led percentage via PWM pulses
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.
#

import sys
from .Adafruit_PWM_Servo_Driver import PWM

MAX_COLOR_LEVEL = 255       # we use RGB color space only here (0-255)
MAX_PULSE_WIDTH = 4095      # equals max color LED brightness

class LED:
    _pwm = None
    _debug = False

    def __init__(self, address=0x40, freq=1000, debug=False):
        # set debug level
        self._debug = debug
        # Initialise the PWM device using the default address
        # from Adafruit: 0x40
        self._pwm = PWM(address, debug)
        # Set frequency in Hz; the default 1000 works with my demo
        self._pwm.setPWMFreq(freq)

    def set_led_level(self, channel, level):
        # convert color level in pulse width
        pulse = int((level/MAX_COLOR_LEVEL)*MAX_PULSE_WIDTH)
        # set led level
        self._pwm.setPWM(channel, 0, pulse)
        # confirm
        if self._debug:
            # go to beginning of line, print the prompt
            sys.stdout.write("\r\nColor level on channel {0} "
                             " set to {1:>3}".format(str(channel), str(level)))
            # stay on this line
            sys.stdout.flush()






