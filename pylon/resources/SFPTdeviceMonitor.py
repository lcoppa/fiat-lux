"""SFPTdeviceMonitor standard profile, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_state_64 import SNVT_state_64
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SCPTscanTime import SCPTscanTime
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTdevListEntry import SCPTdevListEntry
from pylon.resources.SCPTdevListDesc import SCPTdevListDesc


class SFPTdeviceMonitor(base.Profile):
    """SFPTdeviceMonitor standard profile.  Device Monitor.  A device monitor
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
        self.datapoints['nvoDeviceAlarm'] = base.Profile.DatapointMember(
            doc=""" """,
            name='nvoDeviceAlarm',
            profile=self,
            number=1,
            datatype=SNVT_state_64,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoRingALastDev'] = base.Profile.DatapointMember(
            doc="""Scan Time.  Device Alarm.""",
            name='nvoRingALastDev',
            profile=self,
            number=3,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingBLastDev'] = base.Profile.DatapointMember(
            doc="""Scan Time.  States of all monitored device.""",
            name='nvoRingBLastDev',
            profile=self,
            number=4,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingARcv'] = base.Profile.DatapointMember(
            doc="""Devices responding on side A.  Shows which devices can be
            reached via side A.""",
            name='nvoRingARcv',
            profile=self,
            number=5,
            datatype=SNVT_state_64,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRingBRcv'] = base.Profile.DatapointMember(
            doc="""Devices responding on side B.  Shows which devices can be
            reached via side B.""",
            name='nvoRingBRcv',
            profile=self,
            number=7,
            datatype=SNVT_state_64,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpScanTime'] = base.Profile.PropertyMember(
            doc="""Scan Time.  Duration in which all devices are being
            queried.""",
            name='cpScanTime',
            profile=self,
            number=2,
            datatype=SCPTscanTime,
            default=b'\x00\x00\x00\x01\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVer',
            profile=self,
            number=3,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVer',
            profile=self,
            number=4,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpDevList'] = base.Profile.PropertyMember(
            doc="""Device list entry.  Device list entry containing the
            address of the device to be monitored.""",
            name='cpDevList',
            profile=self,
            number=5,
            datatype=SCPTdevListEntry,
            flags=base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpDevListDesc'] = base.Profile.PropertyMember(
            doc="""Device list entry description.  Human readable description
            for an entry in the device list.""",
            name='cpDevListDesc',
            profile=self,
            number=6,
            datatype=SCPTdevListDesc,
            flags=base.PropertyFlags.DISABLE,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTdeviceMonitor()
    pass
