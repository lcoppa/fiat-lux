"""appl_cwp_t standard enumeration type, originally defined in resource file
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class appl_cwp_t(base.Enumeration):
    """appl_cwp_t standard enumeration."""

    # Invalid Value.
    CWP_NUL = -1

    # Normal Wash.
    CWP_GENERAL = 0

    # Boil.
    CWP_BOIL = 1

    # Fast Wash.
    CWP_FAST_WASH = 2

    # Lingerie.
    CWP_LINGERIE = 3

    # Wool.
    CWP_WOOL = 4

    # Towel.
    CWP_TOWEL = 5

    # Bed Linens.
    CWP_BED_LINENS = 6

    # Curtain.
    CWP_CURTAIN = 7

    # Rinse and Spin Only.
    CWP_RINSE_SPIN_ONLY = 8

    # Delicate Rinse.
    CWP_DELICATE_RINSE = 9

    # Spin Only.
    CWP_SPIN_ONLY = 10

    # Dry Only.
    CWP_DRY_ONLY = 11

    def __init__(self):
        super().__init__(
            key=65,
            scope=0,
            prefix='CWP_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = appl_cwp_t()
    pass
