"""UFPTnodeObject userdefined profile, originally defined in resource file
set iot 90:00:00:05:00:00:00:00-1.Note this resource is marked as obsolete.
It should not be used for new development, but continued use in existing
designs is permitted."""


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
from pylon.resources.SFPTnodeObject import SFPTnodeObject
from pylon.resources.UNVT_iot_dev_status import UNVT_iot_dev_status
from pylon.resources.UCPTnetworkTiming import UCPTnetworkTiming
from pylon.resources.UNVT_iot_alarm_ack import UNVT_iot_alarm_ack
from pylon.resources.UCPTiotDescription import UCPTiotDescription
from pylon.resources.UCPTloadGroupName import UCPTloadGroupName
from pylon.resources.UCPTiotLocation import UCPTiotLocation
from pylon.resources.UCPTiotName import UCPTiotName
from pylon.resources.UCPTruntimeLimit1 import UCPTruntimeLimit1
from pylon.resources.UCPTruntimeLimit2 import UCPTruntimeLimit2
from pylon.resources.UCPTiotSceneName import UCPTiotSceneName


class UFPTnodeObject(SFPTnodeObject):
    """UFPTnodeObject userdefined profile.  Node object.  IoT device status
    used to report status of a physical device and control the state of the
    functional blocks on the device ."""

    def __init__(self):
        super().__init__()
        self._override_scope(1)
        self.datapoints['nvoDeviceStatus'] = base.Profile.DatapointMember(
            doc="""IoT device status.  """,
            name='nvoDeviceStatus',
            profile=self,
            number=1,
            datatype=UNVT_iot_dev_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpnDeviceStatus':
                base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nvoDeviceStatus output.""",
                    name='cpnDeviceStatus',
                    profile=self,
                    number=8,
                    datatype=UCPTnetworkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviIotAlarmAck'] = base.Profile.DatapointMember(
            doc="""Alarm acknowledgement.  """,
            name='nviIotAlarmAck',
            profile=self,
            number=2,
            datatype=UNVT_iot_alarm_ack,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoIotAckResult'] = base.Profile.DatapointMember(
            doc="""Alarm acknowledgement result.  """,
            name='nvoIotAckResult',
            profile=self,
            number=3,
            datatype=UNVT_iot_alarm_ack,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpDescription'] = base.Profile.PropertyMember(
            doc="""IoT description.  Text description of the device.""",
            name='cpDescription',
            profile=self,
            number=1,
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
        self.properties['cpLoadGroupName'] = base.Profile.PropertyMember(
            doc="""Text load group name.  Name for a load group to be used by
            optional user interface applications;  used to create an array of
            load group names.""",
            name='cpLoadGroupName',
            profile=self,
            number=2,
            datatype=UCPTloadGroupName,
            array_size_min=2,
            array_size_max=64,
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
            mandatory=False
        )
        self.properties['cpLocation'] = base.Profile.PropertyMember(
            doc="""Text location name.  Text location of the device.""",
            name='cpLocation',
            profile=self,
            number=3,
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
        self.properties['cpName'] = base.Profile.PropertyMember(
            doc="""Text name.  Text name for the device.""",
            name='cpName',
            profile=self,
            number=4,
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
        self.properties['cpRuntimeLimit1'] = base.Profile.PropertyMember(
            doc="""First runtime limit.  """,
            name='cpRuntimeLimit1',
            profile=self,
            number=5,
            datatype=UCPTruntimeLimit1,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpRuntimeLimit2'] = base.Profile.PropertyMember(
            doc="""Second runtime limit.  """,
            name='cpRuntimeLimit2',
            profile=self,
            number=6,
            datatype=UCPTruntimeLimit2,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpSceneName'] = base.Profile.PropertyMember(
            doc="""Text name.  Text scene names.""",
            name='cpSceneName',
            profile=self,
            number=7,
            datatype=UCPTiotSceneName,
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
            mandatory=False
        )
        self.properties['cpnIotAlarm'] = base.Profile.PropertyMember(
            doc="""Network timing.  Application-layer network timing
            parameters for the nvoIotAlarm output.""",
            name='cpnIotAlarm',
            profile=self,
            number=9,
            datatype=UCPTnetworkTiming,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._mark_obsolete()
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = UFPTnodeObject()
    pass
