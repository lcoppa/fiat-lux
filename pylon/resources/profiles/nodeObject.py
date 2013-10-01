"""nodeObject standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.obj_request
import pylon.resources.properties.maxSndT
import pylon.resources.datapoints.time_stamp
import pylon.resources.datapoints.alarm
import pylon.resources.datapoints.file_req
import pylon.resources.datapoints.file_status
import pylon.resources.datapoints.file_pos
import pylon.resources.datapoints.address
import pylon.resources.datapoints.alarm_2
import pylon.resources.datapoints.date_event
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.datapoints.log_fx_request
import pylon.resources.datapoints.log_status
import pylon.resources.datapoints.log_fx_status
import pylon.resources.datapoints.log_request
import pylon.resources.properties.nwrkCnfg
import pylon.resources.properties.location
import pylon.resources.properties.devMajVer
import pylon.resources.properties.devMinVer
import pylon.resources.properties.geoLocation


class nodeObject(pylon.resources.base.Profile):
    """nodeObject standard profile.  Node Object.  Allows the function of
    objects within a node to be monitored.  Only one may exist on a node."""

    def __init__(self):
        super().__init__(
            key=0,
            scope=0,
            principal='nvoStatus'
        )
        self.datapoints['nviRequest'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Object request.  Requests a particular mode for a
            particular object in the device.""",
            name='nviRequest',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.obj_request.obj_request,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Object status.  Reports the status of requested object in
            the device.""",
            name='nvoStatus',
            profile=self,
            number=2,
            datatype=pylon.resources.base.obj_status,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxStsSendT':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  Controls the maximum period of
                    time before the object status is transmitted;  Zero (0)
                    means disabled.""",
                    name='nciMaxStsSendT',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSndT.maxSndT,
                    mandatory=False
                )
            }
        )
        self.datapoints['nviTimeSet'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Time setting.  Synchronize the node's internal real time
            clock with an external time source.""",
            name='nviTimeSet',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm output.  Transmits alarm data for each object on a
            node whenever alarm occurs or is cleared, and upon request.""",
            name='nvoAlarm',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.alarm.alarm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviFileReq'] = pylon.resources.base.Profile.DatapointMember(
            doc="""File request.  Requests an operation on a particular
            file.""",
            name='nviFileReq',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.file_req.file_req,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFileStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""File status.  Reports the status of the last requested
            file operation.""",
            name='nvoFileStat',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.file_status.file_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviFilePos'] = pylon.resources.base.Profile.DatapointMember(
            doc="""File position.  Value used to control the position of the
            read/write pointer in a file.""",
            name='nviFilePos',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.file_pos.file_pos,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFileDirectory'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Configuration parameter file directory address.  Address
            for file directory containing descriptors for configuration
            parameter files.""",
            name='nvoFileDirectory',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.address.address,
            mandatory=False,
            polled=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAlarm2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm output 2.  Transmits alarm data for each functional
            block on a device whenever an alarm occurs or is cleared, and
            upon request.  Replaces nvoAlarm.""",
            name='nvoAlarm2',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.alarm_2.alarm_2,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDateEvent'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Date event.  Reports the status of a schedule.  Optional
            input for the node object for devices with Scheduler functional
            blocks.""",
            name='nviDateEvent',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.date_event.date_event,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDateResync'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Date resynchronization request.  Requests an update for
            all defined exceptions via the nviDateEvent input.  Required
            output from the node object for devices with Scheduler functional
            blocks.""",
            name='nvoDateResync',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviClearStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Clear channel statistics.  Reset all channel statistic
            counters by setting nviClearStat to {100, ON} and back to {0,
            OFF}.  Required on devices implementing the Channelmonitor.""",
            name='nviClearStat',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoUpTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device uptime.  Time since the last reboot of the
            device.""",
            name='nvoUpTime',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            polled=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviLogFxReq'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Log file transfer request.  Requests a data log to be
            transferred via FTP.  Must be followed by a stanard FTP request
            to get the data log file.  Required on devices implementing the
            Data Logger functional profile that support data log transfer via
            FTP.""",
            name='nviLogFxReq',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.log_fx_request.log_fx_request,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLogStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Log status.  Reports the current status of a data log.
            Updated based on the cpLogNotificationThreshold value.  Reports
            status only;  alarms reported via Node Object nvoAlarm2 output.
            Required if the Node Object does not include an nvoLogStat
            output.""",
            name='nvoLogStat',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.log_status.log_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLogFxStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Log file transfer status.  Reports the status of a data
            log file transfer using FTP.  Required on devices implementing
            the Data Logger functional profile that support data log transfer
            via FTP.""",
            name='nvoLogFxStat',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.log_fx_status.log_fx_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviLogReq'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Log status request.  Requests the current status of a data
            log.  Status is reported by the nvoLogStat output.  Required on a
            device containing a Node Object with an nvoLogStat output if the
            device implements multiple Data Logger functional blocks.""",
            name='nviLogReq',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.log_request.log_request,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciNetConfig'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Network configuration source.  Indicates whether the node
            will configure itself, or expects a network manager.""",
            name='nciNetConfig',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.nwrkCnfg.nwrkCnfg,
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Identifies the subsystem containing the
            device.  The subsystem may be a simple location name or a
            hierarchical subsystem name.  If a hierarchical subsystem name is
            specified, the subsystem hierarchy components must be separated
            by periods(".").  Periods must not otherwise be used.  Other
            characters that cannot be used in a subsystem name are the
            backslash ("\"), colon (":"), forward slash ("/"), or
            double-quote characters.  For very large networks, subsystem
            numbers may be used instead of subsystem names, for example:
            "1.2.29".""",
            name='nciLocation',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciDevMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Device major version number.  The major version number for
            the device.""",
            name='nciDevMajVer',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.devMajVer.devMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciDevMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Device minor version number.  The minor version number for
            the device.""",
            name='nciDevMinVer',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.devMinVer.devMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['cpLocationGeo'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Geographic Location.  GPS location where the physical
            device is located.  This configuration property is mandatory if
            the SFPToutdoorLuminairController profile is implemented.""",
            name='cpLocationGeo',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.geoLocation.geoLocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTnodeObject'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = nodeObject()
    pass
