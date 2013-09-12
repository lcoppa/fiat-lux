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
Pilon IP-C Server REST API views.

The main contents of this file has moved to modules of the api.views package.
"""

__version__ = "$Revision: #6 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/views.py $


from django.contrib.staticfiles.views import serve
from django.http                      import HttpResponse


__all__ = ['index']


def index(request):
    """
    The index page view.
    """
    return serve(request, 'api/index.html')


def index_old(request):
    content = """
    <h1>Gary's IP-C Server REST API Page</h1>
    What's here:
    <ul>
        <li><a href="">This index page.</a></li>
    </ul>
    """
    return HttpResponse(content)
