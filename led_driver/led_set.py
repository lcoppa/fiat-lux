""" Set led level via PWM pulses
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

DEFAULT_ADDRESS = 0x40      # i2c address for the pwm board
DEFAULT_FREQ = 1000         # in Hz
MAX_CHANNEL_LEVEL = 255     # we use RGB color space only here (0-255)
MAX_PULSE_WIDTH = 4095      # equals max color LED brightness

class LedStrip:

    def __init__(self, address=DEFAULT_ADDRESS, freq=DEFAULT_FREQ, debug=False):
        # set debug level
        self._debug = debug
        # Initialise the PWM device using the default address
        # from Adafruit: 0x40
        self._pwm = PWM(address, debug)
        # Set frequency in Hz; the default 1000 works with my demo
        self._pwm.setPWMFreq(freq)

    def set_channel_level(self, channel, level, max_level=MAX_CHANNEL_LEVEL):
        # convert color level in pulse width
        self._pulse = int((level/max_level)*MAX_PULSE_WIDTH)
        # set led level
        self._pwm.setPWM(channel, 0, self._pulse)
        # confirm
        if self._debug:
            # go to beginning of line, print the prompt
            sys.stdout.write('\r\nColor level on channel {0} '
                             ' set to {1:>3}'.format(str(channel), str(level)))
            # stay on this line
            sys.stdout.flush()






