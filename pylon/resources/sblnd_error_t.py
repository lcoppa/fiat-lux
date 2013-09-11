"""sblnd_error_t standard enumeration type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class sblnd_error_t(base.Enumeration):
    """sblnd_error_t standard enumeration."""

    # Invalid Value.
    SBE_NUL = -1

    # No error.
    SBE_NO_ERROR = 0

    # In progress.
    SBE_IN_PROGRESS = 1

    # Limits.
    SBE_LIMITS = 2

    # Obstacle up.
    SBE_OBSTACLE_UP = 3

    # Obstacle down.
    SBE_OBSTACLE_DOWN = 4

    # Overheat.
    SBE_OVERHEAT = 5

    # Power.
    SBE_POWER = 6

    # Sensor.
    SBE_SENSOR = 7

    # Motor circuit.
    SBE_MOTOR_CIRCUIT = 8

    # Fuse.
    SBE_FUSE = 9

    # Reference lost.
    SBE_REFERENCE_LOST = 10

    # Host communication.
    SBE_HOST_COMM = 11

    # Voltage 1.
    SBE_VOLTAGE_1 = 12

    # Voltage 2.
    SBE_VOLTAGE_2 = 13

    # Controller.
    SBE_CONTROLLER = 14

    def __init__(self):
        super().__init__(
            key=60,
            scope=0,
            prefix='SBE_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = sblnd_error_t()
    pass
