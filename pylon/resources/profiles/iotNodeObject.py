"""iotNodeObject userdefined profile, originally defined in resource file set
iot 90:00:00:05:00:00:00:00-1.Note this resource is marked as obsolete.  It
should not be used for new development, but continued use in existing designs
is permitted."""


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
import pylon.resources.profiles.nodeObject
import pylon.resources.datapoints.iot_dev_status
import pylon.resources.properties.networkTiming
import pylon.resources.datapoints.iot_alarm_ack
import pylon.resources.properties.iotDescription
import pylon.resources.properties.loadGroupName
import pylon.resources.properties.iotLocation
import pylon.resources.properties.iotName
import pylon.resources.properties.runtimeLimit1
import pylon.resources.properties.runtimeLimit2
import pylon.resources.properties.iotSceneName


class iotNodeObject(pylon.resources.profiles.nodeObject.nodeObject):
    """iotNodeObject userdefined profile.  Node object.  IoT device status
    used to report status of a physical device and control the state of the
    functional blocks on the device ."""

    def __init__(self):
        super().__init__()
        self._override_scope(1)
        self.datapoints['nvoDeviceStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""IoT device status.  """,
            name='nvoDeviceStatus',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.iot_dev_status.iot_dev_status,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpnDeviceStatus':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Network timing.  Application-layer network timing
                    parameters for the nvoDeviceStatus output.""",
                    name='cpnDeviceStatus',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.networkTiming.networkTiming,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviIotAlarmAck'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm acknowledgement.  """,
            name='nviIotAlarmAck',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.iot_alarm_ack.iot_alarm_ack,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoIotAckResult'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm acknowledgement result.  """,
            name='nvoIotAckResult',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.iot_alarm_ack.iot_alarm_ack,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpDescription'] = pylon.resources.base.Profile.PropertyMember(
            doc="""IoT description.  Text description of the device.""",
            name='cpDescription',
            profile=self,
            number=1,
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
        self.properties['cpLoadGroupName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text load group name.  Name for a load group to be used by
            optional user interface applications;  used to create an array of
            load group names.""",
            name='cpLoadGroupName',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.loadGroupName.loadGroupName,
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
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text location name.  Text location of the device.""",
            name='cpLocation',
            profile=self,
            number=3,
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
        self.properties['cpName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text name.  Text name for the device.""",
            name='cpName',
            profile=self,
            number=4,
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
        self.properties['cpRuntimeLimit1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""First runtime limit.  """,
            name='cpRuntimeLimit1',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.runtimeLimit1.runtimeLimit1,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpRuntimeLimit2'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Second runtime limit.  """,
            name='cpRuntimeLimit2',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.runtimeLimit2.runtimeLimit2,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpSceneName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Text name.  Text scene names.""",
            name='cpSceneName',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.iotSceneName.iotSceneName,
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
        self.properties['cpnIotAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Network timing.  Application-layer network timing
            parameters for the nvoIotAlarm output.""",
            name='cpnIotAlarm',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.networkTiming.networkTiming,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'UFPTiotNodeObject'
        self._mark_obsolete()
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = iotNodeObject()
    pass
