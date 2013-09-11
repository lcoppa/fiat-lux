"""SFPTstaticProgrammable standard profile, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_program_status import SNVT_program_status
from pylon.resources.SCPTprogSelect import SCPTprogSelect
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTprogSourceLocation import SCPTprogSourceLocation
from pylon.resources.SCPTprogFileIndexes import SCPTprogFileIndexes
from pylon.resources.SCPTprogCmdHistory import SCPTprogCmdHistory
from pylon.resources.SCPTprogStateHistory import SCPTprogStateHistory
from pylon.resources.SCPTnsdsFbIndex import SCPTnsdsFbIndex
from pylon.resources.SCPTprogErrorHistory import SCPTprogErrorHistory
from pylon.resources.SCPTprogName import SCPTprogName
from pylon.resources.SCPTprogRevision import SCPTprogRevision
from pylon.resources.SCPTnvUsage import SCPTnvUsage


class SFPTstaticProgrammable(base.Profile):
    """SFPTstaticProgrammable standard profile.  The Static Programmable
    Device.  A Static Programmable Device is used for flexible solution
    programming in an Open Systems installation to support different
    application cases."""

    def __init__(self):
        super().__init__(
            key=410,
            scope=0,
            principal='nvoProgramStatus'
        )
        self.datapoints['nvoProgramStatus'] = base.Profile.DatapointMember(
            doc="""Program Status.  This input network variable is used to
            indicate the current status of the Program object.""",
            name='nvoProgramStatus',
            profile=self,
            number=1,
            datatype=SNVT_program_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpProgSelect'] = base.Profile.PropertyMember(
            doc="""Program Select.  This configuration property specifies
            which program is selected to be loaded, if the device can store
            multiple programs.""",
            name='cpProgSelect',
            profile=self,
            number=5,
            datatype=SCPTprogSelect,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpPrgObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpPrgObjMajVer',
            profile=self,
            number=1,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpPrgObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpPrgObjMinVer',
            profile=self,
            number=2,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpProgSourceLocation'] = base.Profile.PropertyMember(
            doc="""Source Location.  This configuration property specifies
            the location from where the source file was downloaded to the
            device.""",
            name='cpProgSourceLocation',
            profile=self,
            number=6,
            datatype=SCPTprogSourceLocation,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x52\x84\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpProgFileIndexes'] = base.Profile.PropertyMember(
            doc="""File Indexes.  This configuration property may be
            implemented if the program data is stored in one or more files on
            the device.""",
            name='cpProgFileIndexes',
            profile=self,
            number=7,
            datatype=SCPTprogFileIndexes,
            flags=base.PropertyFlags.CONST,
            default=b'\x03\x03',
            mandatory=False
        )
        self.properties['cpProgCmdHistory'] = base.Profile.PropertyMember(
            doc="""Command History.  This configuration property contains a
            read-only list of the most recent commands to the device, along
            with a time stamp for each.""",
            name='cpProgCmdHistory',
            profile=self,
            number=8,
            datatype=SCPTprogCmdHistory,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpProgStateHistory'] = base.Profile.PropertyMember(
            doc="""State History.  This configuration property contains a
            read-only list of the most recent state of the device, along with
            a time stamp for each.""",
            name='cpProgStateHistory',
            profile=self,
            number=9,
            datatype=SCPTprogStateHistory,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpFBlockIndex'] = base.Profile.PropertyMember(
            doc="""Index of Functional Block.  The Functional Block index
            within the Node Self-Documentation string to which this program
            applies.""",
            name='cpFBlockIndex',
            profile=self,
            number=10,
            datatype=SCPTnsdsFbIndex,
            minimum=b'\x00\x01',
            default=b'\x00\x01',
            mandatory=False
        )
        self.properties['cpProgErrorHistory'] = base.Profile.PropertyMember(
            doc="""Error History.  Log of recent errors, with time stamp.""",
            name='cpProgErrorHistory',
            profile=self,
            number=11,
            datatype=SCPTprogErrorHistory,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpProgName'] = base.Profile.PropertyMember(
            doc="""Program Name.  This configuration property specifies the
            human-readable name of the currently loaded program.""",
            name='cpProgName',
            profile=self,
            number=3,
            datatype=SCPTprogName,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpProgRevision'] = base.Profile.PropertyMember(
            doc="""Program Revision.  This configuration property specifies
            the revision number of the currently loaded program.""",
            name='cpProgRevision',
            profile=self,
            number=4,
            datatype=SCPTprogRevision,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpNVUsage'] = base.Profile.PropertyMember(
            doc="""NV usage.  The SCPTnvUsage CPs shall be used to indicate
            whether the NVs are in use by the loaded program.""",
            name='cpNVUsage',
            profile=self,
            number=12,
            datatype=SCPTnvUsage,
            default=b'\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTstaticProgrammable()
    pass
