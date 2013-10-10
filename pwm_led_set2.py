""" Set led level via PWM pulses
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.
#

# standard python modules
import sys
import colorsys
import math

# IoT datapoint types used by this application
import pylon.resources.enumerations.color_encoding_t as ColorEncoding
import pylon.resources.enumerations.load_control_t as LoadControl

# I/O pwm driver
from .pylon.examples.common.adafruit.Adafruit_PWM_Servo_Driver import PWM

DEBUG = False
DEFAULT_I2C_ADDRESS = 0x40      # i2c address for the pwm chip
DEFAULT_PWM_FREQ = 1000         # Default frequency in Hz
MAX_CHANNEL_LEVEL = 255         # RGB color space only here (0-255)
MAX_CHANNEL_NUMBER = 16         # Maximum channel number
MAX_PULSE_WIDTH = 4095          # Maximum color LED brightness
NO_PULSE_WIDTH = 0              # Zero LED brightness
PULSE_START = 0                 # Pulse start at zero and lasts pulse_width
LEVEL_ZERO = 0                  # Zero LED brightness


class PwmStripDriver:

    # Set debug level
    _debug = DEBUG

    try:
        # Initialise the PWM chip
        _pwm = PWM(DEFAULT_I2C_ADDRESS, DEBUG)
        # Set frequency in Hz
        _pwm.setPWMFreq(DEFAULT_PWM_FREQ)
    except Exception as e:
        print('Cannot initialise the LED driver on I2C address '
              + str(DEFAULT_I2C_ADDRESS))

    # Set initial pulse widths to 0 for all channels
    _current_pulse_width = []
    for channel_number in range(MAX_CHANNEL_NUMBER):
        _pwm.setPWM(channel_number, PULSE_START, NO_PULSE_WIDTH)
        _current_pulse_width.append(NO_PULSE_WIDTH)

    @staticmethod
    def set_channel_level(channel, level, max_level=MAX_CHANNEL_LEVEL):
        # Convert color level to pulse width
        channel_pulse_width = int((level/max_level)*MAX_PULSE_WIDTH)

        # Test for change
        if channel_pulse_width != PwmStripDriver._current_pulse_width[channel]:
            # Set the new led level
            PwmStripDriver._pwm.setPWM(channel, PULSE_START, channel_pulse_width)
            PwmStripDriver._current_pulse_width[channel] = channel_pulse_width

        if PwmStripDriver._debug:
            # Debug output -- go to beginning of line and print the prompt
            sys.stdout.write('\r\nColor level on channel {0}'
                             ' set to {1:>3}'.format(str(channel), str(level)))
            # Stay on this line
            sys.stdout.flush()

    @staticmethod
    def cleanup():
        # reset all pwm channels to zero
        for channel_number in range(MAX_CHANNEL_NUMBER):
            PwmStripDriver._pwm.setPWM(channel_number, PULSE_START, NO_PULSE_WIDTH)
            PwmStripDriver._current_pulse_width.append(NO_PULSE_WIDTH)


RED_LED_PWM_CHANNEL_OFFSET = 0          # Used by the LED object
GREEN_LED_PWM_CHANNEL_OFFSET = 1        # Used by the LED object
BLUE_LED_PWM_CHANNEL_OFFSET = 2         # Used by the LED object
PWM_CHANNELS_PER_LED = 3                # Used by the LED object
MAX_LEDs = 2                            # Number of hw LEDs supported

MIN_BRIGHTNESS_LEVEL = 0
MAX_BRIGHTNESS_LEVEL = 255
MIN_LUMINANCE_LEVEL = 0                 # Used in HLS color space
MAX_LUMINANCE_LEVEL = 255               # Used in HLS color space
MIN_HUE_LEVEL = 0
MAX_HUE_LEVEL = 255
MIN_SATURATION_LEVEL = 0
MAX_SATURATION_LEVEL = 255
MIN_RED_LEVEL = 0
MAX_RED_LEVEL = 255
MIN_GREEN_LEVEL = 0
MAX_GREEN_LEVEL = 255
MIN_BLUE_LEVEL = 0
MAX_BLUE_LEVEL = 255

DIMMING_STEP = 3                        # Step value when dimming up or down
HUE = 0                                 # Index for hue coordinate in HLS tuple
LUMINANCE = 1                           # Index for luminance coordinate in HLS tuple
SATURATION = 2                          # Index for saturation coordinate in HLS tuple
RED = 0                                 # Index for red coordinate in RGB tuple
GREEN = 1                               # Index for green coordinate in RGB tuple
BLUE = 2                                # Index for blue coordinate in RGB tuple
INVALID_SCENE = 65535                   # Value for no scene

class RGBLed:

    def __init__(self, led_index, debug=False):

        self._debug = debug

        # index of this LED on the pwm board
        self._this_led_index = led_index

        # reset to OFF this LED
        PwmStripDriver.set_channel_level((led_index*PWM_CHANNELS_PER_LED)+RED_LED_PWM_CHANNEL_OFFSET,
                                         LEVEL_ZERO)
        PwmStripDriver.set_channel_level((led_index*PWM_CHANNELS_PER_LED)+GREEN_LED_PWM_CHANNEL_OFFSET,
                                         LEVEL_ZERO)
        PwmStripDriver.set_channel_level((led_index*PWM_CHANNELS_PER_LED)+BLUE_LED_PWM_CHANNEL_OFFSET,
                                         LEVEL_ZERO)

    def set_led_status_and_propagate(self, state, level,
                                     color_type,
                                     red, green, blue,
                                     scene_number,
                                     led_block):
        """ Set the state, level, and color for this LED and update
            the nvoLoadStatus accordingly
        """

        # Shortcut
        nvo_data = led_block.nvoLoadStatus.data


        # if state is on, set color
        if state:

            # compute the new color
            normalised_rgb = self._normalize_led_settings(level, red, green, blue)

            # try to set the new color
            try:
                self._set_led_output(normalised_rgb[RED],
                                     normalised_rgb[GREEN],
                                     normalised_rgb[BLUE])
            except Exception as e:
                print("Cannot set RGB color for led {0}".format(self._this_led_index))
                print(e)

            # if no exceptions, propagate the changes
            else:
                nvo_data.state = state

                # if color encoding is specified, color gets priority on level
                if color_type == ColorEncoding.color_encoding_t.COLOR_RGB:
                    # clear level and propagate color
                    nvo_data.level = float('nan')
                    nvo_data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
                    nvo_data.color.color_value.RGB.red = normalised_rgb[RED]
                    nvo_data.color.color_value.RGB.green = normalised_rgb[GREEN]
                    nvo_data.color.color_value.RGB.blue = normalised_rgb[BLUE]

                # if color not specified and the level is specified, propagate the level
                elif nvo_data.level >= 0.:
                    level = max(level, MIN_BRIGHTNESS_LEVEL)
                    level = min(level, MAX_BRIGHTNESS_LEVEL)
                    nvo_data.level = level

                # if scene has valid value, propagate it
                if nvo_data.scene_number != INVALID_SCENE:
                    nvo_data.scene_number = scene_number

        # if state is off, set black
        else:
            try:
                self._set_rgb_color(0, 0, 0)
            except Exception as e:
                print("Cannot turn off RGB led {0}".format(self._this_led_index))
                print(e)

            # if no exceptions, propagate only the state, leave the rest as is
            else:
                nvo_data.state = state

    def _normalize_led_settings(self, level, r, g, b):
        """ Normalize the state, level, and color for an LED block
        so that they are consistent with each other
        """
        # normalised values
        new_level = 0
        new_r = 0
        new_b = 0
        new_g = 0

        # get the color and check the level
        red_coordinate = float(r) / float(MAX_RED_LEVEL)
        green_coordinate = float(g) / float(MAX_GREEN_LEVEL)
        blue_coordinate = float(b) / float(MAX_BLUE_LEVEL)
        is_black = \
            True if red_coordinate + blue_coordinate + green_coordinate == 0. \
                else False
        print('Normalize LED settings for {0}R:{1}G:{2}B, is_black={3}, and level={4}'.format(
              r, g, b, is_black, level))

        # if level is not specified or invalid (it can be negative for other good reasons)
        if math.isnan(level) or level < 0.:
            # check the color
            if is_black:
                # If color is black; set to white and set level to 100%
                # TODO: why??????????????
                new_r = MAX_RED_LEVEL
                new_g = MAX_GREEN_LEVEL
                new_b = MAX_BLUE_LEVEL
                new_level = float(MAX_BRIGHTNESS_LEVEL)
            else:
                # Color specified; set the level from the color
                hls_color = colorsys.rgb_to_hls(red_coordinate,
                                                green_coordinate,
                                                blue_coordinate)
                new_level = \
                    float((hls_color[LUMINANCE]/MAX_LUMINANCE_LEVEL)*MAX_BRIGHTNESS_LEVEL)
            print('Level not specified; new level is {0}'.format(new_level))

        # If level is specified
        else:
            print('Level specified as {0}'.format(level))
            if level == 0.:
                # State is on but level if 0; set the level to 100%
                new_level = float(MAX_BRIGHTNESS_LEVEL)
                print('Level changed from 0 to {0}'.format(new_level))
            if is_black:
                # State is on but color is black; set to white then adjust the level
                red_coordinate = 1.0
                green_coordinate = 1.0
                blue_coordinate = 1.0

        # Level and color specified; adjust color to match the level
        print('Adjusted level is {0}'.format(new_level))
        lightness_coordinate = new_level / float(MAX_BRIGHTNESS_LEVEL)

        hls_color = colorsys.rgb_to_hls(red_coordinate,
                                        green_coordinate,
                                        blue_coordinate)

        adjusted_rgb = colorsys.hls_to_rgb(hls_color[HUE],
                                           lightness_coordinate,
                                           hls_color[SATURATION])

        nvo_data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
        new_r = int(adjusted_rgb[RED] * 255.)
        new_g = int(adjusted_rgb[GREEN] * 255.)
        new_b = int(adjusted_rgb[BLUE] * 255.)

        print('Adjusted color: {0}H:{1}L:{2}S, {3}R:{4}G:{5}B, {6}HLS'.format(
              hls_color[HUE], lightness_coordinate, hls_color[SATURATION],
              adjusted_rgb[RED], adjusted_rgb[GREEN], adjusted_rgb[BLUE], hls_color))

        return tuple(new_r, new_g, new_b, new_level)























        pass

    def propagate(self, led_block):
        """ Normalize the state, level, and color for an LED block so that they are
        consistent with each other when the state is on.  No changes are made if the
        state is off. """

        # Shortcut
        nvo_data = led_block.nvoLoadStatus.data

        nvo_data.control = LoadControl.load_control_t.LOAD_REPORT
        if nvo_data.state:
            # State is on; get the color and check the level
            red_coordinate = float(nvo_data.color.color_value.RGB.red) / float(MAX_RED_LEVEL)
            green_coordinate = float(nvo_data.color.color_value.RGB.green) / float(MAX_GREEN_LEVEL)
            blue_coordinate = float(nvo_data.color.color_value.RGB.blue) / float(MAX_BLUE_LEVEL)
            is_black = True if red_coordinate + blue_coordinate + green_coordinate == 0. else False
            print('Normalize LED settings for {0}R:{1}G:{2}B, is_black={3}, and level={4}'.format(
                    red_coordinate, green_coordinate, blue_coordinate,
                    is_black, nvo_data.level))
            if math.isnan(nvo_data.level) or \
                            nvo_data.level < 0.:
                # Level not specified; check the color
                if is_black:
                    # Color is black; set to white and set level to 100%
                    nvo_data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
                    nvo_data.color.color_value.RGB.red = MAX_RED_LEVEL
                    nvo_data.color.color_value.RGB.green = MAX_GREEN_LEVEL
                    nvo_data.color.color_value.RGB.blue = MAX_BLUE_LEVEL
                    nvo_data.level = float(MAX_BRIGHTNESS_LEVEL)
                else:
                    # Color specified; set the level from the color
                    hls_color = colorsys.rgb_to_hls(red_coordinate,
                                                    green_coordinate, blue_coordinate)
                    nvo_data.level = \
                        float((hls_color[LUMINANCE]/MAX_LUMINANCE_LEVEL)*MAX_BRIGHTNESS_LEVEL)
                print('Level not specified; new level is {0}'.format(
                        nvo_data.level))
            else:
                # Level specified
                print('Level specified as {0}'.format(nvo_data.level))
                if nvo_data.level == 0.:
                    # State is on but level if 0; set the level to 100%
                    nvo_data.level = float(MAX_BRIGHTNESS_LEVEL)
                    print('Level changed from 0 to {0}'.format(nvo_data.level))
                if is_black:
                    # State is on but color is black; set to white then adjust the level
                    red_coordinate = 1.0
                    green_coordinate = 1.0
                    blue_coordinate = 1.0
            # Level and color specified; adjust color to match the level
            print('Adjusted level is {0}'.format(nvo_data.level))
            lightness_coordinate = nvo_data.level / float(MAX_BRIGHTNESS_LEVEL)
            hls_color = colorsys.rgb_to_hls(red_coordinate, green_coordinate, blue_coordinate)
            adjusted_rgb = colorsys.hls_to_rgb(hls_color[HUE], lightness_coordinate, hls_color[SATURATION])
            nvo_data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
            nvo_data.color.color_value.RGB.red = int(adjusted_rgb[RED] * 255.)
            nvo_data.color.color_value.RGB.green = int(adjusted_rgb[GREEN] * 255.)
            nvo_data.color.color_value.RGB.blue = int(adjusted_rgb[BLUE] * 255.)
            print('Adjusted color: {0}H:{1}L:{2}S, {3}R:{4}G:{5}B, {6}HLS'.format(
                  hls_color[HUE], lightness_coordinate, hls_color[SATURATION],
                  adjusted_rgb[RED], adjusted_rgb[GREEN], adjusted_rgb[BLUE], hls_color))

    def _set_led_output(self, led_block):
        """ Set the state for an LED channel based on the nvoLoadStatus settings.
        Call normalize_led_state() first to normalize the settings. """

        # Shortcut
        nvo_data = led_block.nvoLoadStatus.data

        if nvo_data.state:
            # State is on; set color
            self._set_rgb_color(nvo_data.color.color_value.RGB.red,
                                nvo_data.color.color_value.RGB.green,
                                nvo_data.color.color_value.RGB.blue)
        else:
            # State is off; set black
            self._set_rgb_color(0, 0, 0)

    def _set_rgb_color(self, r, g, b):
        """ Set RGB 0-255 values for the specified LED """

        print('Set PWM LED {0} RGB color to {1}R:{2}G:{3}B'.format(
              self._this_led_index, r, g, b))
        PwmStripDriver.set_channel_level((self._this_led_index *
                                          PWM_CHANNELS_PER_LED) +
                                         RED_LED_PWM_CHANNEL_OFFSET,
                                         r)
        PwmStripDriver.set_channel_level((self._this_led_index *
                                          PWM_CHANNELS_PER_LED) +
                                         GREEN_LED_PWM_CHANNEL_OFFSET,
                                         g)
        PwmStripDriver.set_channel_level((self._this_led_index *
                                          PWM_CHANNELS_PER_LED)+
                                         BLUE_LED_PWM_CHANNEL_OFFSET,
                                         b)


