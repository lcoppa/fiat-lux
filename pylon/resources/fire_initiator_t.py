"""fire_initiator_t standard enumeration type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class fire_initiator_t(base.Enumeration):
    """fire_initiator_t standard enumeration."""

    # Invalid Value.
    FI_NUL = -1

    # Initiator is undefined.
    FI_UNDEFINED = 0

    # Initiator is thermal fixed (heat).
    FI_THERMAL_FIXED = 1

    # Initiator is smoke and ion.
    FI_SMOKE_ION = 2

    # Initiator is multi-ion and thermal.
    FI_MULTI_ION_THERMAL = 3

    # Initiator is smoke and photo.
    FI_SMOKE_PHOTO = 4

    # Initiator is multi-photo and thermal.
    FI_MULTI_PHOTO_THERMAL = 5

    # Initiator is multi-photo and ion.
    FI_MULTI_PHOTO_ION = 6

    # Initiator is multi-photo, ion and thermal.
    FI_MULTI_PHOTO_ION_THERMAL = 7

    # Initiator is thermal fixed and Rate of Rise.
    FI_THERMAL_ROR = 8

    # Initiator is multi-thermal and Rate of Rise.
    FI_MULTI_THERMAL_ROR = 9

    # Initiator is manual pull.
    FI_MANUAL_PULL = 10

    # Initiator is water flow.
    FI_WATER_FLOW = 11

    # Initiator is water flow and tamper.
    FI_WATER_FLOW_TAMPER = 12

    # Initiator is status only.
    FI_STATUS_ONLY = 13

    # Initiator is a manual call point.
    FI_MANUAL_CALL = 14

    # Initiator is a fireman call point.
    FI_FIREMAN_CALL = 15

    # General purpose initiator definition.
    FI_UNIVERSAL = 16

    def __init__(self):
        super().__init__(
            key=27,
            scope=0,
            prefix='FI_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = fire_initiator_t()
    pass
