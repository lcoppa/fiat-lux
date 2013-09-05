#!/usr/bin/env python3
"""A simple pilon performance test.

This test script creates a simple output datapoint, configures itself, binds
the datapoint to issue a single domain broadcast message with every update,
then updates this output datapoint as quickly as possible.

The datapoint implements a 4-byte floating point variable.

The script updates the datapoint for a configurable number of times (command
line argument), tracks total time, success and failure, and reports simple
statistics in the end.

Test method: Send 4-byte output datapoint in loop using unrepeated domain
broadcast on a 3-byte domain Id. Await completion of previous transaction
prior to starting next attempt.

Run 1, 7-Aug-2013, pre-alpha-5, x86 / debug mode
Completed 5000 iterations in 5000 attempts with 5000 successes, 0 failures
(100.0% good) in 0:00:10.753038, yield 464.98487218216843 updates/s

Run 2, 7-Aug-2013, pre-alpha-5, x86 / full release
Completed 5000 iterations in 5000 attempts with 5000 successes, 0 failures
(100.0% good) in 0:00:06.756666, yield 740.0099398135116 updates/s

Run 3, 7-Aug-2013, pre-alpha-5, Raspberry Pi / full release, SSH console
Completed 5000 iterations in 5000 attempts with 5000 successes, 0 failures
(100.0% good) in 0:00:31.874368, yield 156.86585534809663 updates/s

Run 3, 7-Aug-2013, pre-alpha-5, Raspberry Pi / full release, native console (no X11)
Completed 5000 iterations in 5000 attempts with 5000 successes, 0 failures
(100.0% good) in 0:00:33.964537, yield 147.21237036147437 updates/s

"""
#
# This application is for internal use only.
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#

#
# Importing required standard Python modules.
#
import argparse
import datetime
import logging
import select
import sys

#
# Import pylon
#
import pylon
import pylon.interface
import pylon.system

#
# Importing pylon resources used by this application
#
from pylon.resources.SNVT_ppm_f import SNVT_ppm_f


def main():
    """The script's main function"""

    def menu(app):
        sys.stdout.flush()
        while True:
            app.service()

            #
            #   Interactive user input
            #
            i, o, e = select.select([sys.stdin], [], [], 0.01)
            if i:
                try:
                    selection = sys.stdin.readline().strip().lower()
                    if selection == 'exit':
                        print('Winding down...', end='')
                        sys.stdout.flush() # print(flush=True() req. Python3.3
                        app.stop()
                        print(' done')
                        exit()
                    elif selection == 'go':
                        break
                    elif selection == 'service':
                        app.send_service_message()
                    else:
                        print('Valid commands are "exit", "go", "service"')
                except Exception as e:
                    print(e)

    #
    #	Say hi
    #
    print("Welcome to the Pylon performance test 1 Application.")

    #
    #   Command line arguments:
    #
    parser = argparse.ArgumentParser(
        description="The Pilon performance test 1 script"
    )
    parser.add_argument(
        '-d', '--device',
        required=True,
        help='The device URI, e.g. //10.0.1.12/uc'
    )
    parser.add_argument(
        '-D', '--debug',
        default=False,
        action='store_true',
        help='Enables full trace logging'
    )
    parser.add_argument(
        '-i', '--iterations',
        default=1000,
        type=int,
        help='Specify the number of iterations'
    )
    parser.add_argument(
        '-l', '--log',
        default='minidemo',
        help='The base location and name for log files'
    )
    parser.add_argument(
        '-n', '--nvd',
        default='minidemo-nvd',
        help='Path to non-volatile data storage (folder)'
    )
    parser.add_argument(
        '-o', '--domain',
        default='49:53:49',
        type=str,
        help='Colon-separated domain Id'
    )
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:10:9A:01',
        help='The colon-separated program ID'
    )

    arguments = parser.parse_args()
    print("Setting up...", end="")

    #
    #   The pilon application object:
    #
    app = pylon.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )

    #
    #   Create the output, success/failure counters and completion event
    #   handler
    #
    output = app.output_datapoint(
        data=SNVT_ppm_f(),
        name='test data'
    )

    success = 0
    failure = 0
    attempts = 0

    def output_complete(sender, args):
        if isinstance(args, pylon.interface.Datapoint.OnCompletionEventArgs):
            if args.result:
                nonlocal success
                success += 1
            else:
                nonlocal failure
                failure += 1
        if success + failure < arguments.iterations:
            output.propagate()
            nonlocal attempts
            attempts += 1

    output.OnComplete += output_complete

    #
    #   Start pilon:
    #
    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId

    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        if app.isi:
            app.isi.tracefile(arguments.log + '-isi.log', False)

    app.start()

    #
    #   Configure self:
    #
    domain = pylon.system.Domain()
    domain.domain_id = arguments.domain
    domain.is_valid = True
    domain.subnet_id = 20
    domain.node_id = 21
    domain.is_cloned = False

    address = pylon.system.BroadcastAddress()
    address.domain = 0
    address.subnet = 0

    dpcfg = pylon.system.DatapointConfig()
    dpcfg.output = True
    dpcfg.selector = 0
    dpcfg.service_type = pylon.system.ServiceType.UNACKNOWLEDGED
    dpcfg.address_index = 0

    app.system.update_datapoint_config(output, dpcfg)
    app.system.update_address(0, address)
    app.system.update_domain(0, domain)

    app.system.go_configured()
    app.system.go_online()

    if arguments.iterations < 2:
        raise ValueError(
            'Can\' iterate over less than 2 iterations.'
        )

    print(
        " done. Enter a command now (e.g. 'service', 'exit' or 'go'): ",
        end=""
    )

    menu(app)

    print("Running test..", end="")
    sys.stdout.flush() # print(flush=True() req. Python3.3

    start = datetime.datetime.now()
    attempts += 1
    output.propagate()

    #
    #   Run the application:
    #
    try:

        while success + failure < arguments.iterations:

            #
            #   Service pilon
            #
            app.service()

    finally:

        end = datetime.datetime.now()

        #
        #   Stop pilon
        #
        app.stop()

        print(' done.')
        print(
            'Completed {0} iterations in {1} attempts with {2} successes, '
            '{3} failures\n'
            '({4}% good) in {5}, yield {6} updates/s'.format(
                arguments.iterations,
                attempts,
                success,
                failure,
                100*success/arguments.iterations,
                end-start,
                success / (end-start).total_seconds()
            )
        )

        print("Good bye.")

if __name__ == '__main__':
    main()
