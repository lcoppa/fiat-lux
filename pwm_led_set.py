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
from pylon.examples.common.adafruit.Adafruit_PWM_Servo_Driver import PWM

DEFAULT_ADDRESS = 0x40      # i2c address for the pwm chip
DEFAULT_FREQ = 1000         # Default frequency in Hz
MAX_CHANNEL_LEVEL = 255     # RGB color space only here (0-255)
MAX_CHANNEL_NUMBER = 16     # Maximum channel number
MAX_PULSE_WIDTH = 4095      # Maximum color LED brightness
NO_PULSE_WIDTH = 0          # Zero LED brightness
PULSE_START = 0             # Pulse start at zero and lasts pulse_width


class LedStrip:

    def __init__(self, address=DEFAULT_ADDRESS, freq=DEFAULT_FREQ, debug=False):
        # Set debug level
        self._debug = debug
        # Initialise the PWM chip
        self._pwm = PWM(address, debug)
        # Set frequency in Hz
        self._pwm.setPWMFreq(freq)

        # Set initial pulse widths to 0 for all channels
        self._pulse_width = []
        for channel_number in range(MAX_CHANNEL_NUMBER):
            self._pulse_width.append(NO_PULSE_WIDTH)
            self._pwm.setPWM(channel_number, PULSE_START, NO_PULSE_WIDTH)

    def set_channel_level(self, channel, level, max_level=MAX_CHANNEL_LEVEL):
        # Convert color level to pulse width
        pulse_width = int((level/max_level)*MAX_PULSE_WIDTH)

        # Test for change
        if pulse_width != self._pulse_width[channel]:
            # Set the new led level
            self._pulse_width[channel] = pulse_width
            self._pwm.setPWM(channel, PULSE_START, pulse_width)

        if self._debug:
            # Debug output -- go to beginning of line and print the prompt
            sys.stdout.write('\r\nColor level on channel {0} '
                             ' set to {1:>3}'.format(str(channel), str(level)))
            # Stay on this line
            sys.stdout.flush()

    def cleanup(self):
        # reset all pwm channels to zero
        for channel_number in range(MAX_CHANNEL_NUMBER):
            self._pwm.setPWM(channel_number, PULSE_START, NO_PULSE_WIDTH)









