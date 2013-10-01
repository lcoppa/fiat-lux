"""iotAnalogOutput userdefined profile, originally defined in resource file
set iot 90:00:00:05:00:00:00:00-1."""


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
import pylon.resources.datapoints.iot_analog
import pylon.resources.properties.defInput
import pylon.resources.properties.highLimDly
import pylon.resources.properties.highLimit1
import pylon.resources.properties.highLimit1Enable
import pylon.resources.properties.highLimit2
import pylon.resources.properties.highLimit2Enable
import pylon.resources.properties.lowLimDly
import pylon.resources.properties.lowLimit1
import pylon.resources.properties.lowLimit1Enable
import pylon.resources.properties.lowLimit2
import pylon.resources.properties.lowLimit2Enable
import pylon.resources.properties.networkTiming
import pylon.resources.properties.iotDescription
import pylon.resources.properties.eventAlgorithmInhibit
import pylon.resources.properties.eventDetectionEnable
import pylon.resources.properties.iotName
import pylon.resources.properties.iotLocation
import pylon.resources.properties.reliabilityEvaluationInhibit


class iotAnalogOutput(pylon.resources.base.Profile):
    """iotAnalogOutput userdefined profile.  Analog output.  IoT actuator,
    monitoring device, or application receiving inputs from analog sensors or
    applications ."""

    def __init__(self):
        super().__init__(
            key=20001,
            scope=1,
            principal='nviAnalog'
        )
        self.datapoints['nviAnalog'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Analog datapoint.  Analog value with units, timestamp,
            status, and priority.""",
            name='nviAnalog',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.iot_analog.iot_analog,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'cpDefaultInput':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default input.  The level the analog input should
                    adopt when expected updates are not received and at
                    power-on reset.""",
                    name='cpDefaultInput',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.defInput.defInput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimitDelay':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit delay.  The time limit during normal
                    operation before a high alarm is recognized.""",
                    name='cpHighLimitDelay',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.highLimDly.highLimDly,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 1.  The alarm first high limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpHighLimit1',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit1Enable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 1 Enable.  Controls whether high limit
                    1 is in effect.""",
                    name='cpHighLimit1Enable',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.highLimit1Enable.highLimit1Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpHighLimit2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 2.  The alarm second high limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpHighLimit2',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.highLimit2.highLimit2,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit2Enable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""High limit 2 Enable.  Controls whether high limit
                    2 is in effect.""",
                    name='cpHighLimit2Enable',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.highLimit2Enable.highLimit2Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpLowLimitDelay':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit delay.  The time limit during normal
                    operation before a low alarm is recognized.""",
                    name='cpLowLimitDelay',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.lowLimDly.lowLimDly,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit1':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 1.  The alarm first low limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpLowLimit1',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.lowLimit1.lowLimit1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit1Enable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 1 Enable.  Controls whether low limit 1
                    is in effect.""",
                    name='cpLowLimit1Enable',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.lowLimit1Enable.lowLimit1Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpLowLimit2':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 2.  The alarm second low limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpLowLimit2',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.lowLimit2.lowLimit2,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit2Enable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Low limit 2 Enable.  Controls whether low limit 2
                    is in effect.""",
                    name='cpLowLimit2Enable',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.lowLimit2Enable.lowLimit2Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpnAnalog':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nviAnalog input.""",
                    name='cpnAnalog',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.networkTiming.networkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.properties['cpDescription'] = pylon.resources.base.Profile.PropertyMember(
            doc="""IoT description.  Text description for the analog
            datapoint.""",
            name='cpDescription',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.iotDescription.iotDescription,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpEventAlgorithmInhibit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Event algorithm inhibit.  Inhibit the event algorithm if
            true.""",
            name='cpEventAlgorithmInhibit',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.eventAlgorithmInhibit.eventAlgorithmInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpEventDetectionEnable'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Event detection enable.  Enable event detection if
            true.""",
            name='cpEventDetectionEnable',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.eventDetectionEnable.eventDetectionEnable,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text name.  Text name for the analog datapoint.""",
            name='cpName',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.iotName.iotName,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text location name.  Location of the analog datapoint.""",
            name='cpLocation',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.iotLocation.iotLocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpReliabilityEvaluationInhibit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Reliability evaluation inhibit.  Inhibit reliability
            evaluation if true.""",
            name='cpReliabilityEvaluationInhibit',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.reliabilityEvaluationInhibit.reliabilityEvaluationInhibit,
            default=b'\x00',
            mandatory=True
        )
        self._original_name = 'UFPTiotAnalogOutput'
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = iotAnalogOutput()
    pass
