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
Pylon IP-C Server REST API query parameters.
"""

__version__ = "$Revision: #4 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/query_params.py $


__all__ = ['QUERY_DEPTH', 'QUERY_REFTYPE']


# Depth.  How many levels to expand results.  Default: 0.
QUERY_DEPTH = {
    'PARAM':    'depth',
    'DEFAULT':  0
}

# Reference Type.  The type of referenced objects.
# One of: 'id', 'url'.  Default: 'url'.
QUERY_REFTYPE = {
    'PARAM':    'ref_type',
    'DEFAULT':  'url',
    
    'URL':      'url',
    'ID':       'id'
}
