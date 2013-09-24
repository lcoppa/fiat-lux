"""sblnd_cmd_source_t standard enumeration type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class sblnd_cmd_source_t(base.Enumeration):
    """sblnd_cmd_source_t standard enumeration."""

    # Invalid value.
    SBCS_NUL = -1

    # Local.
    SBCS_LOCAL = 0

    # Group.
    SBCS_GROUP = 1

    # Wind speed.
    SBCS_WIND_SPEED = 2

    # Sun lux level.
    SBCS_SUN_LUX = 3

    # Rain.
    SBCS_RAIN = 4

    # Frost.
    SBCS_FROST = 5

    # Dawn.
    SBCS_DAWN = 6

    # Dusk.
    SBCS_DUSK = 7

    # Outside temperature.
    SBCS_OUTSIDE_TEMP = 8

    # Indoor temperature.
    SBCS_INDOOR_TEMP = 9

    # Outdoor relative humidity.
    SBCS_OUTDOOR_RH = 10

    # Indoor relative humidity.
    SBCS_INDOOR_RH = 11

    # Illumination level.
    SBCS_ILLUM_LEVEL = 12

    # Scene.
    SBCS_SCENE = 13

    # Global.
    SBCS_GLOBAL = 14

    # Window contact.
    SBCS_WINDOW_CONTACT = 15

    # Auto-mode changed.
    SBCS_AUTOMODE_CHANGED = 16

    # Override.
    SBCS_OVERRIDE = 17

    # Emergency.
    SBCS_EMERGENCY = 18

    # Maintenance.
    SBCS_MAINTENANCE = 19

    # Intrusion.
    SBCS_INTRUSION = 20

    # Terminal load.
    SBCS_TERMINAL_LOAD = 21

    # Alarm.
    SBCS_ALARM = 22

    # Occupancy sensor.
    SBCS_OCC_SENSOR = 23

    # Occupancy manual command.
    SBCS_OCC_MAN_CMD = 24

    # Glare.
    SBCS_GLARE = 25

    # Alarm 2.
    SBCS_ALARM_2 = 26

    # Notify.
    SBCS_NOTIFY = 27

    # Elevation.
    SBCS_ELEVATION = 28

    # Azimuth.
    SBCS_AZIMUTH = 29

    # Set override.
    SBCS_SET_OVERRIDE = 30

    # Set maintenance.
    SBCS_SET_MAINTENANCE = 31

    # Timer.
    SBCS_TIMER = 32

    # Unknown command source.
    SBCS_UNKNOWN = 127

    def __init__(self):
        super().__init__(
            key=59,
            scope=0,
            prefix='SBCS_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = sblnd_cmd_source_t()
    pass
