"""elevatorArrivalGong standard profile, originally defined in resource file
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
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.count
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.location
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.nwrkCnfg
import pylon.resources.properties.installedLevel


class elevatorArrivalGong(pylon.resources.base.Profile):
    """elevatorArrivalGong standard profile.  Elevator/Lift Arrival Gong.
    Indicates the arrival of the elevator car at the landing.  The gong is
    activated only at the landing where the car is stopping."""

    def __init__(self):
        super().__init__(
            key=14013,
            scope=0
        )
        self.datapoints['nviUpGong'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Up direction signal.  Instructs the gong to sound an 'UP'
            indication.""",
            name='nviUpGong',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFloorLevel'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Location of elevator car.  Location of the elevator car --
            used for the scenario where all the gongs are bound to the same
            direction output-network-variables.""",
            name='nviFloorLevel',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDownGong'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Down direction signal.  Instructs the gong to sound a
            'DOWN' indication.""",
            name='nviDownGong',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciMaxReceiveT'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciMaxReceiveT',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            maximum=b'\x01\x2c',
            default=b'\x00\x64',
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciNetCnfg'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Network configuration source.  The value of this field
            determines the source of the node's network configuration.""",
            name='nciNetCnfg',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.nwrkCnfg.nwrkCnfg,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciInstLevel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Installed level.  The floor or level on which the device
            is installed.""",
            name='nciInstLevel',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.installedLevel.installedLevel,
            mandatory=False
        )
        self._original_name = 'SFPTelevatorArrivalGong'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = elevatorArrivalGong()
    pass
