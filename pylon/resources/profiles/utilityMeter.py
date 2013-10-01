"""utilityMeter standard profile, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.reg_val_ts
import pylon.resources.properties.sndDelta
import pylon.resources.properties.timePeriod
import pylon.resources.datapoints.time_stamp
import pylon.resources.properties.location
import pylon.resources.properties.baseValue
import pylon.resources.properties.pulseValue
import pylon.resources.properties.numDigits
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class utilityMeter(pylon.resources.base.Profile):
    """utilityMeter standard profile.  Utility Meter.  To register measuring
    information from utility meters for remote metering."""

    def __init__(self):
        super().__init__(
            key=2201,
            scope=0
        )
        self.datapoints['nvoMeterVal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Meter Value Output.  This network variable contains the
            present value of the meter, i.e., the actual running value hown
            by the display on the meter.""",
            name='nvoMeterVal',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.reg_val_ts.reg_val_ts,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSendOnDelta':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Send on delta.  The minimum change required to
                    force transmission of the output value.""",
                    name='nciSendOnDelta',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.sndDelta.sndDelta,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoHistVal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Historical Value Output.  This network variable contains,
            by default, a copy of the valid meter value at the turn of the
            last month.""",
            name='nvoHistVal',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.reg_val_ts.reg_val_ts,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciHistPeriod':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Historical Period.  This input configuration
                    network variable defines the period of time between
                    transfer of a values to the historical register.""",
                    name='nciHistPeriod',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.timePeriod.timePeriod,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviHistTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Historical-Time Selection Input.  This input network
            variable controls which history value is shown on the output
            network variable:  nvoHistVal.""",
            name='nviHistTime',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciStartVal'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Base value.  The base value (where to begin counting)""",
            name='nciStartVal',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.baseValue.baseValue,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciPulseConst'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Pulse and Transformer Constant.  This configuration
            property is used to scale the raw pulse value to an energy-meter
            value.""",
            name='nciPulseConst',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.pulseValue.pulseValue,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciNumDigits'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Number of Digits on the Meter.  This configuration
            property is used for setting the total number of digits on the
            meter.""",
            name='nciNumDigits',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.numDigits.numDigits,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=7,
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
            number=8,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTutilityMeter'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = utilityMeter()
    pass
