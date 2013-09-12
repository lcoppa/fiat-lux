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
Pilon IP-C Server server initialization.
"""

__version__ = "$Revision: #4 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/project/server.py $


import logging

from shared import *

__all__     = ['start_server']


# The string to set as the process title,
# to more easily identify this process in ps-like listing.
# Requires the 'setproctitle' package to be installed.
PROCESS_TITLE = '[IP-C Server]'


# our logger
logger = logging.getLogger(NAMESPACE('project.server'))


def set_process_title(title):
    """
    set the process title,
    as long as the 'setproctitle' package is available
    """

    # try to import the 'setproctitle' package
    try:
        from setproctitle import setproctitle
    except ImportError:
        # package not located 
        # - ignore the error and return (the process title will not be changed)
        return

    # set the process title
    logger.debug("Setting the process title to: %r", title)
    setproctitle(title)


def attach_debugger(host=None):
    """
    Attach to a PyDev debugger on host <host>
    (default: value of PYDEV_HOST environment variable).
    Returns <True> on success, otherwise <False>.
    """

    import os, sys
    
    # determine debugger host
    if not host:
        host = os.getenv('PYDEV_HOST')
        if not host:
            #print('Error: Debugger host not specified (either on command line or via PYDEV_HOST environment variable).\n', file=sys.stderr)
            return False
    
    # attempt to attach to the debugger
    try:
        import pydevd  # NOTE: only imported if needed (some people may not have/want PyDev installed)
        pydevd.settrace(host, stdoutToServer=True, stderrToServer=True, suspend=False, trace_only_current_thread=False)
        print("[attached to PyDev debugger on host '{}']".format(host))
    except Exception as e:
        #print("Error: Failed to attach to PyDev debugger on host '{}': {}".format(host, e), file=sys.stderr)
        return False
    
    return True


# IP-C Server startup
logger.info("Starting Pilon IP-C Server...")

def start_server():
    """
    Start the IP-C Server.
    """
    
    # forced debugger - e.g. for debugging command line parsing
    attach_debugger()
    
    # attempt to set process title
    if PROCESS_TITLE:
        set_process_title(PROCESS_TITLE)
    
    # create and start the IP-C Server collectors
    from collectors.collector import Collector
    Collector.create_collectors()
