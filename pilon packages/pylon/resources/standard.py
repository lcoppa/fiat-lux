"""
    standard - a pre-defined and re-usable Drf definition object
"""

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

from pylon.resources import base

standard = base.Drf(
    program_id='00:00:00:00:00:00:00:00',
    scope=0,
    name='standard',
    version=(14, 0),
    doc="""
    This file is the standard type file, containing Standard Network Variable
    Types (SNVTs), Standard Configuration Property Types (SCPTs), and the
    enumeration types that support them. This file was created and is
    maintained by LonMark International. Contact LonMark International at
    +1-408-938-5266, at www.lonmark.org, or at 550 Meridian Ave, San Jose CA
    95126, USA."""
)
