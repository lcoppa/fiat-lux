"""pilon.resources

This sub-package contains definitions for datapoint types, property types and
profiles standardized by LonMark International, and some non-standard
definitions maintained by Echelon Corporation.

See http://types.lonmark.org or http://types.echelon.com for an online
reference guide of these definitions (Microsoft Internet Explorer required).

"""
# ### TODO REMINDER describe how one can add other user-defined resources

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import sys

# noinspection PyUnresolvedReferences
import pylon.resources.base


def version_check(minimum):
    major, minor, micro, level, serial = sys.version_info
    if major < minimum:
        raise ImportError(
            'pylon requires Python version {0}.0.0 or better'.format(minimum)
        )


version_check(3)

# noinspection PyUnresolvedReferences
__all__ = [
    'base'
]
