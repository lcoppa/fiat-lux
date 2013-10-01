"""clothesWasherDomestic standard profile, originally defined in resource
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.clothes_w_c
import pylon.resources.datapoints.clothes_w_s
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.time_min
import pylon.resources.datapoints.clothes_w_a
import pylon.resources.datapoints.clothes_w_m
import pylon.resources.properties.ahamApplianceModel
import pylon.resources.properties.location
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class clothesWasherDomestic(pylon.resources.base.Profile):
    """clothesWasherDomestic standard profile.  Clothes Washer, Domestic.
    Residential clothes washer for units with or without integrated an
    dryer."""

    def __init__(self):
        super().__init__(
            key=15011,
            scope=0
        )
        self.datapoints['nviWasherCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Washer Command Input.  Contains all required information
            for clothes-washer control.""",
            name='nviWasherCmd',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.clothes_w_c.clothes_w_c,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoWasherStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Washer Status Output.  Contains the present status of a
            washer.""",
            name='nvoWasherStatus',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.clothes_w_s.clothes_w_s,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviPowerOnOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power On/Off Input.  Commands a washer to turn-on or
            turn-off.""",
            name='nviPowerOnOff',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoPowerOnOffAct'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power On/Off Report Output.  Commands a washer to turn-on
            or turn-off.""",
            name='nvoPowerOnOffAct',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviStartStop'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Washing Start/Stop Input.  Commands the washer to begin or
            halt the programmed/commanded cycle.""",
            name='nviStartStop',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoStartStopAct'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Washing Start/Stop Report Output.  Reports the washer's
            actual state of operation.""",
            name='nvoStartStopAct',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTimeTotalRem'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total Time Remaining Output.  This output network variable
            provides the total remaining time before the entire wash process
            is complete.""",
            name='nvoTimeTotalRem',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.time_min.time_min,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAlarmRpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm-Status Report Output.  This output network variable
            provides duplicate information of the alarm field of
            nvoWasherStatus.""",
            name='nvoAlarmRpt',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.clothes_w_a.clothes_w_a,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoManageStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Washer-Management Status Output.  This output network
            variable provides the status of the door/lid and the drain.""",
            name='nvoManageStatus',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.clothes_w_m.clothes_w_m,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciApplianceMod'] = pylon.resources.base.Profile.PropertyMember(
            doc="""AHAM Appliance Model.  Appliance Model code as defined by
            the Association of Home Appliance Manufacturers.""",
            name='nciApplianceMod',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.ahamApplianceModel.ahamApplianceModel,
            flags=pylon.resources.base.PropertyFlags.CONST,
            minimum=b'\x00',
            maximum=b'\x00',
            default=b'\x00',
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=4,
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
            number=5,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTclothesWasherDomestic'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = clothesWasherDomestic()
    pass
