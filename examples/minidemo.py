#!/usr/bin/env python3
"""A simple pilon demo application.

   The simple demo implements a SFPTopenLoopActuator and SFPTopenLoopSensor
   profile pair, both using a SNVT_temp_p datapoint type for fixed-point
   temperature values. Both profiles implement all mandatory datapoint and
   property members.

   When the actuator receives a new input temperature value, half of this
   value is reported through the actuator's output. Both values are shown on
   the console.

   The pilon framework also implements a SPFTnodeObject profile as required,
   and supplies basic node object functionality.

"""
#
# This application is for internal use only.
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#

#
# Importing required standard Python modules.
#
import argparse
import logging
import select
import sys

#
# Import pylon
#
import pylon.device

#
# Importing pylon resources used by this application
#
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SFPTopenLoopActuator import SFPTopenLoopActuator


def main():
    """The script's main function"""

    #
    #	Say hi
    #
    print("Welcome to the Pylon MiniDemo Application.")
    print("Enter 'exit' to exit, or 'service' to send a service message.\n")

    #
    #   Command line arguments:
    #
    parser = argparse.ArgumentParser(
        description="The Pilon mini demo script"
    )
    parser.add_argument(
        '-d', '--device',
        required=True,
        help='The device URI, e.g. uc://10.0.1.12:1628'
    )
    parser.add_argument(
        '-n', '--nvd',
        default='minidemo-nvd',
        help='Path to non-volatile data storage (folder)'
    )
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:00:9A:81',
        help='The colon-separated program ID'
    )
    parser.add_argument(
        '-l', '--log',
        default='minidemo',
        help='The base location and name for log files'
    )
    parser.add_argument(
        '-D', '--debug',
        default=False,
        action='store_true',
        help='Enables full trace logging'
    )

    arguments = parser.parse_args()

    #
    #   The pilon application object:
    #
    app = pylon.device.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )

    #
    # Create the two blocks. Mandatory members are automatically implemented.
    #
    sensor = app.block(
        profile=SFPTopenLoopSensor(),
        ext_name='ols',
        snvt_xxx=SNVT_temp_p
    )
    actuator = app.block(
        profile=SFPTopenLoopActuator(),
        ext_name='ola',
        snvt_xxx=SNVT_temp_p
    )

    #
    #   Handle updates to the actuator's input:
    #
    # noinspection PyUnusedLocal
    def update_handler(sender, arguments):
        with sensor.nvoValue, actuator.nviValue:
            sensor.nvoValue.data = 0.5 * actuator.nviValue.data
            print('Update received and processed: {0} = 0.5 * {1}'.format(
                sensor.nvoValue.data,
                actuator.nviValue.data
            ))

    actuator.nviValue.OnUpdate += update_handler

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
    #   Run the application:
    #
    try:
        done = False

        while not done:

            #
            #   Service pilon
            #
            app.service()

            #
            #   Interactive user input
            #
            i, o, e = select.select([sys.stdin], [], [], 0.01)
            if i:
                try:

                    selection = sys.stdin.readline().strip().lower()
                    if selection == 'exit':
                        print('Winding down...')
                        done = True
                    elif selection == 'service':
                        app.send_service_message()
                    elif selection == 'wink':
                        # Simulate receipt of a Wink message for testing:
                        app.OnWink.fire(app, None)
                    else:
                        print(
                            'Valid commands are "exit", "service", "wink"'
                        )
                except Exception as e:
                    print(e)
    finally:

        #
        #   Stop pilon
        #
        app.stop()
        print("Good bye.")


if __name__ == '__main__':
    main()
