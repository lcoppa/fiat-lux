"""telephoneDirectory standard profile, originally defined in resource file
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.char_ascii
import pylon.resources.datapoints.str_asc
import pylon.resources.properties.dialString


class telephoneDirectory(pylon.resources.base.Profile):
    """telephoneDirectory standard profile.  Telephone Directory.  A
    Telephone Directory is used to store and retreive arrays of ASCII strings
    that are characterized as telephone numbers (including characters used
    for control) used in dialing a data modem."""

    def __init__(self):
        super().__init__(
            key=5092,
            scope=0
        )
        self.datapoints['nviReqDialStr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Request Dial String Input.  Telephone-number entry index
            (0-to-maximum), where maximum is less than or equal to 255.""",
            name='nviReqDialStr',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.char_ascii.char_ascii,
            mandatory=True,
            minimum=b'\x00',
            maximum=b'\xff',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDialStr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dial String Output.  Character string (30 characters
            max)""",
            name='nvoDialStr',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.str_asc.str_asc,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciDialStr'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Dial string.  Telephone number string used in dialing,
            including characters used for control.""",
            name='nciDialStr',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.dialString.dialString,
            array_size_max=256,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self._original_name = 'SFPTtelephoneDirectory'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = telephoneDirectory()
    pass
