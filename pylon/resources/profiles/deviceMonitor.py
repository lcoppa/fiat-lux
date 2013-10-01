"""deviceMonitor standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.state_64
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.count
import pylon.resources.properties.scanTime
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.devListEntry
import pylon.resources.properties.devListDesc


class deviceMonitor(pylon.resources.base.Profile):
    """deviceMonitor standard profile.  Device Monitor.  A device monitor
    functional profile is used to monitor the health state of other devices
    in the network by periodically polling them using query status network
    diagnostic messages.  If a device goes (soft) offline or is no longer
    reachable over the network, an alarm is generated and output network
    variables can be used to determine the state of all monitored nodes."""

    def __init__(self):
        super().__init__(
            key=136,
            scope=0
        )
        self.datapoints['nvoDeviceAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc=""" """,
            name='nvoDeviceAlarm',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.state_64.state_64,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoRingALastDev'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scan Time.  Device Alarm.""",
            name='nvoRingALastDev',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingBLastDev'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scan Time.  States of all monitored device.""",
            name='nvoRingBLastDev',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingARcv'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Devices responding on side A.  Shows which devices can be
            reached via side A.""",
            name='nvoRingARcv',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.state_64.state_64,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingBRcv'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Devices responding on side B.  Shows which devices can be
            reached via side B.""",
            name='nvoRingBRcv',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.state_64.state_64,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpScanTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scan Time.  Duration in which all devices are being
            queried.""",
            name='cpScanTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.scanTime.scanTime,
            default=b'\x00\x00\x00\x01\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVer',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVer',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpDevList'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Device list entry.  Device list entry containing the
            address of the device to be monitored.""",
            name='cpDevList',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.devListEntry.devListEntry,
            array_size_min=128,
            array_size_max=128,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpDevListDesc'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Device list entry description.  Human readable description
            for an entry in the device list.""",
            name='cpDevListDesc',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.devListDesc.devListDesc,
            array_size_min=128,
            array_size_max=128,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTdeviceMonitor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = deviceMonitor()
    pass
