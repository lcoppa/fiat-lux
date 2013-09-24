"""UFPTiotAnalogInput userdefined profile, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1."""


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
# Generated at 12-Sep-2013 11:24.

from pylon.resources import base
from pylon.resources.userdefined import userdefined
from pylon.resources.UNVT_iot_analog import UNVT_iot_analog
from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.SCPThighLimDly import SCPThighLimDly
from pylon.resources.SCPThighLimit1 import SCPThighLimit1
from pylon.resources.SCPThighLimit1Enable import SCPThighLimit1Enable
from pylon.resources.SCPThighLimit2 import SCPThighLimit2
from pylon.resources.SCPThighLimit2Enable import SCPThighLimit2Enable
from pylon.resources.SCPTlowLimDly import SCPTlowLimDly
from pylon.resources.SCPTlowLimit1 import SCPTlowLimit1
from pylon.resources.SCPTlowLimit1Enable import SCPTlowLimit1Enable
from pylon.resources.SCPTlowLimit2 import SCPTlowLimit2
from pylon.resources.SCPTlowLimit2Enable import SCPTlowLimit2Enable
from pylon.resources.UCPTnetworkTiming import UCPTnetworkTiming
from pylon.resources.UCPTiotDescription import UCPTiotDescription
from pylon.resources.UCPTeventAlgorithmInhibit import UCPTeventAlgorithmInhibit
from pylon.resources.UCPTeventDetectionEnable import UCPTeventDetectionEnable
from pylon.resources.UCPTiotName import UCPTiotName
from pylon.resources.UCPTiotLocation import UCPTiotLocation
from pylon.resources.UCPTreliabilityEvaluationInhibit import UCPTreliabilityEvaluationInhibit


class UFPTiotAnalogInput(base.Profile):
    """UFPTiotAnalogInput userdefined profile.  Analog input.  IoT sensor or
    application reporting an analog value ."""

    def __init__(self):
        super().__init__(
            key=20000,
            scope=1,
            principal='nvoAnalog'
        )
        self.datapoints['nvoAnalog'] = base.Profile.DatapointMember(
            doc="""Analog datapoint.  Analog value with units, timestamp,
            status, and priority.""",
            name='nvoAnalog',
            profile=self,
            number=1,
            datatype=UNVT_iot_analog,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpDefaultOutput':
                base.Profile.PropertyMember(
                    doc="""Default output.  The level the analog datapoint
                    should adopt when expected updates are not received and
                    at power-on reset.""",
                    name='cpDefaultOutput',
                    profile=self,
                    number=1,
                    datatype=SCPTdefOutput,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimitDelay':
                base.Profile.PropertyMember(
                    doc="""High limit delay.  The time limit during normal
                    operation before a high alarm is recognized.""",
                    name='cpHighLimitDelay',
                    profile=self,
                    number=5,
                    datatype=SCPThighLimDly,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit1':
                base.Profile.PropertyMember(
                    doc="""High limit 1.  The alarm first high limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpHighLimit1',
                    profile=self,
                    number=6,
                    datatype=SCPThighLimit1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit1Enable':
                base.Profile.PropertyMember(
                    doc="""High limit 1 Enable.  Controls whether high limit
                    1 is in effect.""",
                    name='cpHighLimit1Enable',
                    profile=self,
                    number=7,
                    datatype=SCPThighLimit1Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpHighLimit2':
                base.Profile.PropertyMember(
                    doc="""High limit 2.  The alarm second high limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpHighLimit2',
                    profile=self,
                    number=8,
                    datatype=SCPThighLimit2,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpHighLimit2Enable':
                base.Profile.PropertyMember(
                    doc="""High limit 2 Enable.  Controls whether high limit
                    2 is in effect.""",
                    name='cpHighLimit2Enable',
                    profile=self,
                    number=9,
                    datatype=SCPThighLimit2Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpLowLimitDelay':
                base.Profile.PropertyMember(
                    doc="""Low limit delay.  The time limit during normal
                    operation before a low alarm is recognized.""",
                    name='cpLowLimitDelay',
                    profile=self,
                    number=10,
                    datatype=SCPTlowLimDly,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit1':
                base.Profile.PropertyMember(
                    doc="""Low limit 1.  The alarm first low limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpLowLimit1',
                    profile=self,
                    number=11,
                    datatype=SCPTlowLimit1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit1Enable':
                base.Profile.PropertyMember(
                    doc="""Low limit 1 Enable.  Controls whether low limit 1
                    is in effect.""",
                    name='cpLowLimit1Enable',
                    profile=self,
                    number=12,
                    datatype=SCPTlowLimit1Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpLowLimit2':
                base.Profile.PropertyMember(
                    doc="""Low limit 2.  The alarm second low limit against
                    which the present_value field of the output value is
                    tested for alarm conditions.""",
                    name='cpLowLimit2',
                    profile=self,
                    number=13,
                    datatype=SCPTlowLimit2,
                    default=b'\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpLowLimit2Enable':
                base.Profile.PropertyMember(
                    doc="""Low limit 2 Enable.  Controls whether low limit 2
                    is in effect.""",
                    name='cpLowLimit2Enable',
                    profile=self,
                    number=14,
                    datatype=SCPTlowLimit2Enable,
                    default=b'\x00',
                    mandatory=True
                ),
                'cpnAnalog':
                base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nvoAnalog output.""",
                    name='cpnAnalog',
                    profile=self,
                    number=18,
                    datatype=UCPTnetworkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.properties['cpDescription'] = base.Profile.PropertyMember(
            doc="""IoT description.  Text description for the analog
            datapoint.""",
            name='cpDescription',
            profile=self,
            number=2,
            datatype=UCPTiotDescription,
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
        self.properties['cpEventAlgorithmInhibit'] = base.Profile.PropertyMember(
            doc="""Event algorithm inhibit.  Inhibit the event algorithm if
            true.""",
            name='cpEventAlgorithmInhibit',
            profile=self,
            number=3,
            datatype=UCPTeventAlgorithmInhibit,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpEventDetectionEnable'] = base.Profile.PropertyMember(
            doc="""Event detection enable.  Enable event detection if
            true.""",
            name='cpEventDetectionEnable',
            profile=self,
            number=4,
            datatype=UCPTeventDetectionEnable,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpName'] = base.Profile.PropertyMember(
            doc="""Text name.  Text name for the analog datapoint.""",
            name='cpName',
            profile=self,
            number=15,
            datatype=UCPTiotName,
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
        self.properties['cpLocation'] = base.Profile.PropertyMember(
            doc="""Text location name.  Location of the analog sensor.""",
            name='cpLocation',
            profile=self,
            number=16,
            datatype=UCPTiotLocation,
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
        self.properties['cpReliabilityEvaluationInhibit'] = base.Profile.PropertyMember(
            doc="""Reliability evaluation inhibit.  Inhibit evaluation of
            block reliability;  sets the reliability field to
            REL_NO_FAULT_DETECTED.""",
            name='cpReliabilityEvaluationInhibit',
            profile=self,
            number=17,
            datatype=UCPTreliabilityEvaluationInhibit,
            default=b'\x00',
            mandatory=True
        )
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = UFPTiotAnalogInput()
    pass
