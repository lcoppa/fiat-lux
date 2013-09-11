"""SFPTutilityDataLoggerRegister standard profile, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_reg_val_ts import SNVT_reg_val_ts
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SNVT_time_stamp import SNVT_time_stamp
from pylon.resources.SNVT_reg_val import SNVT_reg_val
from pylon.resources.SNVT_lev_disc import SNVT_lev_disc
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SCPTregName import SCPTregName
from pylon.resources.SCPThighLimit1 import SCPThighLimit1
from pylon.resources.SCPTsndDelta import SCPTsndDelta
from pylon.resources.SCPTbaseValue import SCPTbaseValue


class SFPTutilityDataLoggerRegister(base.Profile):
    """SFPTutilityDataLoggerRegister standard profile.  Utility Data-Logger
    Register.  Used to report energy use from an energy meter."""

    def __init__(self):
        super().__init__(
            key=2110,
            scope=0,
            principal='nvoRegVal'
        )
        self.datapoints['nvoRegVal'] = base.Profile.DatapointMember(
            doc="""Register value output.  This network variable contains the
            current value of the register with a time stamp and status bits
            all contained within one variab.""",
            name='nvoRegVal',
            profile=self,
            number=1,
            datatype=SNVT_reg_val_ts,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviHistChoice'] = base.Profile.DatapointMember(
            doc="""Register historical period selection input.  This input
            network variable controls which history value is shown on the
            output network variable side via the network variables voHistVal
            and nvoHistTime.""",
            name='nviHistChoice',
            profile=self,
            number=2,
            datatype=SNVT_count,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHistTime'] = base.Profile.DatapointMember(
            doc="""Register historical time selection input.  This input
            network variable controls, according to the time, which history
            value is shown on the output network variable side via the
            network variables nvoHistVal and nvoHistTime.""",
            name='nviHistTime',
            profile=self,
            number=3,
            datatype=SNVT_time_stamp,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRegVal'] = base.Profile.DatapointMember(
            doc="""Register value input.  A value can be sent to the register
            object via the network using this network variable.""",
            name='nviRegVal',
            profile=self,
            number=4,
            datatype=SNVT_reg_val,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRegState'] = base.Profile.DatapointMember(
            doc="""Register state selection input.  The register can be
            activated or deactivated by using this variable.  When a register
            is activated the register object measures into the register.  If
            the register is deactivated it does not measure but it is
            read/write-able.""",
            name='nviRegState',
            profile=self,
            number=5,
            datatype=SNVT_lev_disc,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEndPeriod'] = base.Profile.DatapointMember(
            doc="""Measuring period ending input.  This input network
            variable controls the ending of a billing period.  When the
            billing period is terminated, the current register value will be
            transferred to the next history register.  The series register
            cannot use this roperty.""",
            name='nviEndPeriod',
            profile=self,
            number=6,
            datatype=SNVT_time_stamp,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoHistVal'] = base.Profile.DatapointMember(
            doc="""Register historical value output.  This output network
            variable contains the register object's historical value of a
            chosen time or history period.  The output value is selected
            using the nviHistChoice or nviHistTime variables.""",
            name='nvoHistVal',
            profile=self,
            number=7,
            datatype=SNVT_reg_val_ts,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoHistTime'] = base.Profile.DatapointMember(
            doc="""Register historical time output.  This output network
            variable contains a billing period end time.  The output value is
            selected using the nviHistChoice and nviHistTime variables.""",
            name='nvoHistTime',
            profile=self,
            number=8,
            datatype=SNVT_time_stamp,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMeasPeriod'] = base.Profile.DatapointMember(
            doc="""Register measuring period output.  This output network
            variable contains the length of the measuring period.  If used,
            the register object measures series or maximum value data.
            Otherwise the value is zero.""",
            name='nvoMeasPeriod',
            profile=self,
            number=9,
            datatype=SNVT_elapsed_tm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciRegName'] = base.Profile.PropertyMember(
            doc="""Register name.  The name of a utility data logger register
            device.""",
            name='nciRegName',
            profile=self,
            number=1,
            datatype=SCPTregName,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciHLimit'] = base.Profile.PropertyMember(
            doc="""High limit 1.  The alarm high limit against which the
            value field of the output value is tested for alarm
            conditions.""",
            name='nciHLimit',
            profile=self,
            number=2,
            datatype=SCPThighLimit1,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciSendOnDelta'] = base.Profile.PropertyMember(
            doc="""Send on delta.  The minimum change required to force
            transmission of the output value.""",
            name='nciSendOnDelta',
            profile=self,
            number=3,
            datatype=SCPTsndDelta,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciBaseValue'] = base.Profile.PropertyMember(
            doc="""Base value.  The base value (where to begin counting)""",
            name='nciBaseValue',
            profile=self,
            number=4,
            datatype=SCPTbaseValue,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTutilityDataLoggerRegister()
    pass
