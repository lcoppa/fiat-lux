#
# Copyright (c) 2013 Echelon Corporation.  All rights reserved.
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

"""
Pylon IP-C
"""

# overall package version
VERSION = "0.6.0"

# internal version
__version__ = "$Revision: #2 $"
# $File: //depot/Software/Pylon/Dev/Releases/alpha-6/pylon-0.6.0/pylon/__init__.py $


import sys

# noinspection PyUnresolvedReferences
import pylon.device


# noinspection PyUnresolvedReferences
__all__ = [
    'VERSION',
    'device',
    'resources'
]


def version_check(minimum):
    major, minor, micro, level, serial = sys.version_info
    if major < minimum:
        raise ImportError(
            'pylon requires Python version {0}.0.0 or better'.format(minimum)
        )


version_check(3)
