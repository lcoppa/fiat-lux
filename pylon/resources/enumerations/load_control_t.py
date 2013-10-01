"""load_control_t userdefined enumeration type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1."""


# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software" to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file is generated from device resource files using an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.  The machine-generated code may not meet
# compliance with PEP-8 and PEP-257 recommendations at all times.
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.userdefined import userdefined


class load_control_t(pylon.resources.base.Enumeration):
    """load_control_t userdefined enumeration."""

    # Invalid value.
    LOAD_NUL = -1

    # Report the load state, level, angle, color, multipler, and occupancy
    # settings;  any unused values are set to the invalid value;  used as a
    # reporting output from load controllers;  ignored as input to load
    # controls.
    LOAD_REPORT = 0

    # Set the load to the values specified in the state, level, angle, color,
    # multiplier fields, and occupancy;  any fields set to the invalid value
    # are ignored and not changed in the load;  typically used with lighting,
    # load groups to set the level, color, or multiplier for all lighting
    # loads;  also used with sunblind and fan groups to the set level (and
    # angle for sunblinds) for all sunblinds and fans in the respective
    # group.
    LOAD_SET = 1

    # Toggle the state field value;  typically used with lighting load groups
    # to toggle all lighting loads.
    LOAD_TOGGLE = 2

    # Increment the level and angle by the value specified in the level
    # field;  positive values repesent an increase in level or angle;
    # negative values represent a decrease;  the value is clipped at the
    # limit when a limit is reached;  typically used with lighting load
    # groups to increase the level of all lighting loads;  used with
    # sunblinds to raise/lower, or rotate the angle of all sunblinds;  used
    # with fans to increase or decrease the rotation speed of all fans.
    LOAD_INCREMENT = 3

    # Same as LOAD_INCREMENT, except that the level and angle values are set
    # to the opposite limit when a limit is reached;  for example, a 5%
    # repeating cycle starting at 90% results in the following values:  90%,
    # 95%, 100%, 0%, 5%.
    LOAD_CYCLE = 4

    # Increment the color hue by the value specified in the level field;
    # positive values increase the hue and negative values decrease the hue;
    # typically used with lighting load groups to increase the color hue of
    # all lighting loads.
    LOAD_INCREMENT_HUE = 5

    # Recall the state, level, angle, color, delay, and duration from the
    # specified scene.
    LOAD_RECALL_SCENE = 6

    # Store the specified state, level, angle, color, delay, and duration for
    # the specified scene.
    LOAD_STORE_SCENE = 7

    # Learn the present state, level, angle, color, delay, and duration for
    # the specified scene.
    LOAD_LEARN_SCENE = 8

    # Provide a visible indicator on the selected loads for the specified
    # duration;  the indicator may be the light flashing for a lighting
    # load.
    LOAD_WINK = 9

    # Set scene definitions, load group membership, and settings to the
    # factory default state.
    LOAD_FACTORY_DEFAULTS = 10

    # Stop any motion or changes to the selected loads.
    LOAD_STOP = 11

    def __init__(self):
        super().__init__(
            key=8,
            scope=1,
            prefix='LOAD_'
        )
        self._original_name = 'load_control_t'
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = load_control_t()
    pass
