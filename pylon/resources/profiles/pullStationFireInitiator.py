"""pullStationFireInitiator standard profile, originally defined in resource
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
import pylon.resources.datapoints.switch
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.fire_test
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.properties.location
import pylon.resources.properties.zoneNum
import pylon.resources.properties.oemType
import pylon.resources.properties.installDate
import pylon.resources.properties.maintDate
import pylon.resources.properties.manfDate
import pylon.resources.properties.fireTxt1
import pylon.resources.properties.fireTxt2
import pylon.resources.properties.fireTxt3


class pullStationFireInitiator(pylon.resources.base.Profile):
    """pullStationFireInitiator standard profile.  Pull-Station Fire
    Initiator.  Manual, Pull-Station Fire Initiator object for fire-alarm
    notification and response functions."""

    def __init__(self):
        super().__init__(
            key=11005,
            scope=0
        )
        self.datapoints['nvoFireAlm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fire Alarm.  This outpur NV transmits fire information for
            use by simple Indicators.""",
            name='nvoFireAlm',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoFireTrouble'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fire Trouble.  This output NV transmitted initiator
            trouble information for use by simple Indicators.""",
            name='nvoFireTrouble',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDeviceRequest'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fire test request.  This input NV receives requests
            intended to perform smoke detector operations, initiated from
            operator.""",
            name='nviDeviceRequest',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.fire_test.fire_test,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoEmergMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""HVAC emergency mode.  This input NV controls the
            (actuator) position for smoke control devices.""",
            name='nvoEmergMode',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciNodeLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciNodeLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciZoneNum'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Zone number.  The zone number for the device.""",
            name='nciZoneNum',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.zoneNum.zoneNum,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciOEMLabel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOEMLabel',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.oemType.oemType,
            flags=pylon.resources.base.PropertyFlags.MFG |
                pylon.resources.base.PropertyFlags.CONST,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.installDate.installDate,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaintDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maintenance date.  The date of last maintenance for the
            device.""",
            name='nciMaintDate',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.maintDate.maintDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciManufDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciManufDate',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.manfDate.manfDate,
            flags=pylon.resources.base.PropertyFlags.MFG |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciFireText1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information.  Text information relevant to fire
            conditions.  A '>' at end of string indicates presence of fire
            text 2.""",
            name='nciFireText1',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.fireTxt1.fireTxt1,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciFireText2'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information, continuation.  Continuation text
            information relevant to fire conditions.  A '>' at end of string
            indicates presence of fire text 3.""",
            name='nciFireText2',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.fireTxt2.fireTxt2,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciFireText3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information, second continuation.  Second
            continuation text information relevant to fire conditions.""",
            name='nciFireText3',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.fireTxt3.fireTxt3,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTpullStationFireInitiator'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = pullStationFireInitiator()
    pass
