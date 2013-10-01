"""occupancyController standard profile, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.standard import standard
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.setting
import pylon.resources.properties.location
import pylon.resources.properties.holdTime
import pylon.resources.properties.primeVal
import pylon.resources.properties.secondVal


class occupancyController(pylon.resources.base.Profile):
    """occupancyController standard profile.  Occupancy Controller.  Input is
    the occupancy state, and the output is the control value for an actuator
    (typically a lamp)"""

    def __init__(self):
        super().__init__(
            key=3071,
            scope=0,
            principal='nviOccupancy'
        )
        self.datapoints['nviOccupancy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy status input value.  Provides the occupancy
            status.""",
            name='nviOccupancy',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=True,
            minimum=b'\xff',
            maximum=b'\x01',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLampValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Lamp value output.  State for the lamp actuator (ON or
            OFF), and the percentage level of intensity.""",
            name='nvoLampValue',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSecondary'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary occupancy status input value.  Provides the
            occupancy status of a neighboring area in order to provide
            low-level lighting around an occupied area for a feeling of
            security.""",
            name='nviSecondary',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            minimum=b'\xff',
            maximum=b'\x01',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setting input (Auto/Off) The mode can be either ON(AUTO)
            or OFF.""",
            name='nviSetting',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            minimum=b'\x00\x00\xb9\xb1',
            maximum=b'\x01\xc8\x46\x50',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviManOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Manual override input.  Enables the local and manual
            control of the lamp value output.""",
            name='nviManOverride',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setting output.  Selects the operating mode for another
            controller (e.g., constant light controller)""",
            name='nvoSetting',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciHoldTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Hold time value.  Hold time for occupied state after there
            is no occupancy detected.""",
            name='nciHoldTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.holdTime.holdTime,
            default=b'\x17\x70',
            mandatory=False
        )
        self.properties['nciPrimeVal'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Primary default value.  Default lamp value sent when the
            area is occupied.""",
            name='nciPrimeVal',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.primeVal.primeVal,
            default=b'\xc8\x01',
            mandatory=False
        )
        self.properties['nciSecondVal'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Secondary default value.  Default lamp value sent when the
            neighboring area is occupied.""",
            name='nciSecondVal',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.secondVal.secondVal,
            default=b'\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPToccupancyController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = occupancyController()
    pass
