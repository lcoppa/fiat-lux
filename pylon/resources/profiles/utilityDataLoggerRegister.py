"""utilityDataLoggerRegister standard profile, originally defined in resource
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
import pylon.resources.datapoints.reg_val_ts
import pylon.resources.datapoints.count
import pylon.resources.datapoints.time_stamp
import pylon.resources.datapoints.reg_val
import pylon.resources.datapoints.lev_disc
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.properties.regName
import pylon.resources.properties.highLimit1
import pylon.resources.properties.sndDelta
import pylon.resources.properties.baseValue


class utilityDataLoggerRegister(pylon.resources.base.Profile):
    """utilityDataLoggerRegister standard profile.  Utility Data-Logger
    Register.  Used to report energy use from an energy meter."""

    def __init__(self):
        super().__init__(
            key=2110,
            scope=0,
            principal='nvoRegVal'
        )
        self.datapoints['nvoRegVal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register value output.  This network variable contains the
            current value of the register with a time stamp and status bits
            all contained within one variab.""",
            name='nvoRegVal',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.reg_val_ts.reg_val_ts,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviHistChoice'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register historical period selection input.  This input
            network variable controls which history value is shown on the
            output network variable side via the network variables voHistVal
            and nvoHistTime.""",
            name='nviHistChoice',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHistTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register historical time selection input.  This input
            network variable controls, according to the time, which history
            value is shown on the output network variable side via the
            network variables nvoHistVal and nvoHistTime.""",
            name='nviHistTime',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRegVal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register value input.  A value can be sent to the register
            object via the network using this network variable.""",
            name='nviRegVal',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.reg_val.reg_val,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRegState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register state selection input.  The register can be
            activated or deactivated by using this variable.  When a register
            is activated the register object measures into the register.  If
            the register is deactivated it does not measure but it is
            read/write-able.""",
            name='nviRegState',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.lev_disc.lev_disc,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEndPeriod'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Measuring period ending input.  This input network
            variable controls the ending of a billing period.  When the
            billing period is terminated, the current register value will be
            transferred to the next history register.  The series register
            cannot use this roperty.""",
            name='nviEndPeriod',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoHistVal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register historical value output.  This output network
            variable contains the register object's historical value of a
            chosen time or history period.  The output value is selected
            using the nviHistChoice or nviHistTime variables.""",
            name='nvoHistVal',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.reg_val_ts.reg_val_ts,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHistTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register historical time output.  This output network
            variable contains a billing period end time.  The output value is
            selected using the nviHistChoice and nviHistTime variables.""",
            name='nvoHistTime',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMeasPeriod'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Register measuring period output.  This output network
            variable contains the length of the measuring period.  If used,
            the register object measures series or maximum value data.
            Otherwise the value is zero.""",
            name='nvoMeasPeriod',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciRegName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Register name.  The name of a utility data logger register
            device.""",
            name='nciRegName',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.regName.regName,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciHLimit'] = pylon.resources.base.Profile.PropertyMember(
            doc="""High limit 1.  The alarm high limit against which the
            value field of the output value is tested for alarm
            conditions.""",
            name='nciHLimit',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.highLimit1.highLimit1,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciSendOnDelta'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send on delta.  The minimum change required to force
            transmission of the output value.""",
            name='nciSendOnDelta',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.sndDelta.sndDelta,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciBaseValue'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Base value.  The base value (where to begin counting)""",
            name='nciBaseValue',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.baseValue.baseValue,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTutilityDataLoggerRegister'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = utilityDataLoggerRegister()
    pass
