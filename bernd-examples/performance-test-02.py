#!/usr/bin/env python3
"""A pilon performance test.

This test script creates a simple output and input datapoint pair using a
4-byte floating point variable (SNVT_ppm_f). The script is designed to be
executed on two different devices A and B. The script configures itself.

Once the wind-up and your preparations are complete, enter 'go' at B and enter
'start' at A. (Or the other way around, but this discussion assumes go @ B,
start @ A.)

Both A and B are listening for input datapoint updates. When an update arrives,
each adds 0.01 to the value and propagates the result through the output
datapoint. The script uses the recommended 'with' statement and thread-safe
datapoint locking.

The script configures these devices such that the datapoints are bound using
a simple connection using group addressing. The script can use unrepeated
or acknowledged service.

This creates a datapoint value loop. When B receives an update, it adds 0.01
and pushes the result through the output. This will be received by A, which
in turn adds 0.01 and pushes the result to its output, which will be received
by B, etc.

The 'start' command is necessary to instruct one participant to kick-start the
process by propagating its output.

Test method summary: Send 4-byte value in a circular datapoint loop between
two devices A and B, each receiving an input, applying a simple algorithm and
propagating the result.

Run 1, 7-Aug-2013, pre-alpha-5,

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

    def menu(app, output):
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
                    elif selection == 'start':
                        output.propagate()
                        break
                    else:
                        print(
                            'Valid commands are '
                            '"exit", "go", "service", "start"'
                        )
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
    parser.add_argument(
        '-s', '--service',
        default='unrepeated',
        choices=['unrepeated', 'acknowledged'],
        help='The service type to be used'
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
    #   Create the datapoints, statistic counters and event handlers
    #
    output_datapoint = app.output_datapoint(
        data=SNVT_ppm_f(),
        name='test data'
    )
    input_datapoint = app.input_datapoint(
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

    def input_update(sender, args):
        with input_datapoint, output_datapoint:
            output_datapoint.data = 0.01 + input_datapoint.data
            nonlocal attempts
            attempts += 1

    output_datapoint.OnComplete += output_complete
    input_datapoint.OnUpdate += input_update

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
    domain.is_cloned = True

    address = pylon.system.SubnetNodeAddress()
    address.domain = 0
    address.subnet_id = domain.subnet_id
    address.node_id = domain.node_id

    dpcfg_in = app.system.query_datapoint_config(input_datapoint)
    dpcfg_in.selector = 0

    dpcfg_out = app.system.query_datapoint_config(output_datapoint)
    dpcfg_out.selector = 0
    dpcfg_out.address_index = 0

    if arguments.service == 'unrepeated':
        dpcfg_in.service_type = pylon.system.ServiceType.UNACKNOWLEDGED
        dpcfg_out.service_type = pylon.system.ServiceType.UNACKNOWLEDGED
    else:
        dpcfg_in.service_type = pylon.system.ServiceType.ACKNOWLEDGED
        dpcfg_out.service_type = pylon.system.ServiceType.ACKNOWLEDGED

    app.system.update_datapoint_config(output_datapoint, dpcfg_out)
    app.system.update_datapoint_config(input_datapoint, dpcfg_in)
    app.system.update_address(0, address)
    app.system.update_domain(0, domain)

    app.system.go_configured()
    app.system.go_online()

    if arguments.iterations < 2:
        raise ValueError(
            'Can\' iterate over less than 2 iterations.'
        )

    print(
        " done. Enter a command now ('service', 'exit', 'go' or 'start'): ",
        end=""
    )

    menu(app, output_datapoint)

    print("Running test..", end="")
    sys.stdout.flush()      # print(flush=True() req. Python3.3

    timeout = pylon.toolkit.Timer(app, 120)

    start = datetime.datetime.now()

    #
    #   Run the application:
    #
    try:

        while success + failure < arguments.iterations and \
                not timeout.is_expired:

            #
            #   Service pilon
            #
            app.service()

    finally:

        end = datetime.datetime.now()

        if not timeout.is_running:
            print('Gave up after timeout.')
        else:
            print(' done.')

        #
        #   Stop pilon
        #
        app.stop()

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
