#!/usr/bin/env python3
"""A simple pilon ISI demo application.

    This demo is derived from the minidemo script, and implements the same
    interoperable interface. However, being an ISI demo script, this script
    also uses ISI to connect the open loop sensor and actuator blocks.

    Local turnarounds are supported, but you may also connect between two
    instances of the script.

    Simple Forward Connection:
    --------------------------

    To establish a connection, run at least one instance of the script.
    On the script's console, enter "open 0" to offer enrollment for assembly 0
    ('open 1' for assembly 1, etc). This now becomes the host.
    The following assumes that the host opens enrollment for assembly 0:

    On another instance of the script, or in the same script's console, enter
    'create 1'. This turns it into an enrolled member.

    If you are using only one instance of the script, this will result in a
    turnaround connection.

    (To connect additional instances of the script, visit their console and
    enter 'create 1' on each.)

    On the host, enter 'create 0'. This completes the enrollment process.

    You have now completed a datapoint binding with ISI. The host's sensor
    output is now connected to the member's actuator input datapoint.

    Sensor Readings:
    ----------------

    This simple demo script is designed to work without hardware requirements
    (other than the Raspberry Pi, of course). To simulate a sensor reading,
    enter 'sense 23.5' on the host's console (or any other scaled value valid
    for a SNVT_temp_p, which covers temperature values -273.17...+327.67).

    The member's actuator receives the datapoint value. If it is non-zero, the
    actuator multiplies the value with 0.5 and writes the result into its
    sensor's output datapoint. The process is recorded on the console.

    Because the simple forward connection doesn't connect the sensor's output,
    nothing else happens.

    If you are using a turnaround connection within a single instance of this
    script, or if you are using two or more instances of the same script
    running on the same Raspberry Pi or Linux PC, resulting datapoint update
    messages are routed within the protocol stack. LonScanner or similar
    protocol analysis tools will show the ISI messages used to establish and
    maintain the network, but will not show the datapoint value updates on the
    network. This is normal. You will need to run at least two instances of
    this script on at least two physical devices to expose and monitor
    datapoint updates on the network.

    Adding a Feedback Connection:
    -----------------------------

    You can add a feedback connection to the existing simple connection. This
    connects the sensor's output datapoint to the host's input datapoint.

    To implement the feedback connection, visit the host's console and enter
    'open 1', then enter 'create 0' on the member's console, then complete the
    connection with the 'create 1' command on the host's console.

    Simulating a sensor reading (come on, enter 'sense 173.4' on the host's
    console!) now produces a number of updates, spinning around between host
    and member until the value reached zero. Since the actuator's algorithm
    only works on non-zero values, the madness stops here.

    Deleting Connections:
    ---------------------

    Connections are deleted by making devices leave the connection. When a
    member device leave a connection, the remaining connection remains intact
    even though there might only be one member left. When a host device leaves
    a connection, the connections is deleted and all remaining members are
    asked to leave.

    To delete the feedback connection, for example, enter 'leave 1' on the
    host's console.

    Exercises:
    ----------

    A. No coding required:

    You could now try to re-establish the feedback connection, using the
    forward connection's member as the feedback connection's host.

    You can tell if the connection loop is correct by simulating a sensor
    reading on either of the devices, and observing a series of datapoint
    updates until value zero has been reached.

    You can also use the is_bound command on the console to determine a given
    assembly's connection status, e.g. 'is_connected 1'.

    B. Coding required:

    You can revise the registered Assembly objects and the on_enrollment event
    handler such that a single ISI enrollment creates a complete datapoint loop
    between one host and one member device.

    C. Coding and a little more thought required:

    You can revise exercise (B) such that it supports any number of devices.

    Other commands:
    ---------------

    The script supports a few other commands, notably the 'service' command
    (which issues a service message as well as an ISI DRUM message) and the
    'exit' command to terminate the script.

    Multiple Instances:
    -------------------

    Perhaps this is the first pilon script which tempts you to run multiple
    instances on the same hardware, i.e. three instances of the same script on
    one Raspberry Pi.

    You can do so with the --device, --nvd and --log commands to this script.

    Each instance of the script must have a unique set of device URI,
    persistence path for non-volatile data (NVD) and base name and location for
    log files.

    For example, to start two different instances of this script, you could use

    python3 isi-demo.py --device uc://10.0.1.12:1628 --nvd .isi-demo-A-nvd \
       --log isi-demo-A

    python3 isi-demo.py --device uc://10.0.1.12:1628 --nvd .isi-demo-B-nvd \
       --log isi-demo-B

    (Obviously, you'd need to adjust IP address and port in the device command
    to match your local environment and IP-852 configuration server, or
    provide a suitable multicast-mode device URI.)

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
import time
import socket

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

    def this_pi_ip_addr():
        """ Returns the IP address of this computer.
            Require AVAHID installed (apt-get install avahid) which should
            be installed by default in Raspbian as of summer 2013
        """
        try:
            # get text hostname of the local machine
            host = socket.gethostname()

            # get the numeric IP address from the hostname;
            # this might require avahid
            pi_ip_address = socket.gethostbyname(host + '.local')
            print('Host ' + host + ' has IP address ' + pi_ip_address)

            return pi_ip_address

        except Exception as e:
            print("Can't get IP address")
            print(e)
            # pass the same exception up
            raise
    ### End this_pi_ip_addr function ###


    #
    #	Say hi
    #
    print("Welcome to the Pylon ISI Demo Application.")
    print("Enter 'exit' to exit. Try 'help' for help with other commands.\n")

    def report(me):
        print(
            '{0}: {1}'.format(
                time.asctime(),
                me
            )
        )

    #
    #   Command line arguments:
    #
    parser = argparse.ArgumentParser(
        description="The Pilon ISI demo script"
    )
    parser.add_argument(
            '-d', '--device',
            default='uc://' + this_pi_ip_addr() + ':1628/',
            help='The device URI, e.g. uc://10.0.1.12:1628/')
    # parser.add_argument(
    #     '-d', '--device',
    #     required=True,
    #     help='The device URI, e.g. uc://10.0.1.12:1628'
    # )
    parser.add_argument(
        '-n', '--nvd',
        default='isi-demo-nvd',
        help='Path to non-volatile data storage (folder)'
    )
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:00:9A:90',
        help='The colon-separated program ID'
    )
    parser.add_argument(
        '-l', '--log',
        default='isi-demo',
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
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )

    #
    #   Create the two blocks
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
        if actuator.nviValue.data:
            sensor.nvoValue.data = 0.5 * actuator.nviValue.data
            report(
                'Update received and processed: {0} = 0.5 * {1}'.format(
                    sensor.nvoValue.data,
                    actuator.nviValue.data
                )
            )

    actuator.nviValue.OnUpdate += update_handler

    #
    # ISI Assembly objects, an ols_assembly assembly to match the open loop
    # actuator block, and an ola_assembly assembly to match the open loop
    # sensor block.
    # Note that there is no requirement of a 1:1 relation between blocks and
    # ISI assemblies.
    #
    ols_assembly = pylon.device.isi.Assembly(
        assembly=sensor.nvoValue,
        enrollment=pylon.device.isi.Enrollment(
            direction=pylon.device.isi.IsiDirection.OUTPUT,
            type_id=sensor.nvoValue
        )
    )

    ola_assembly = pylon.device.isi.Assembly(
        assembly=actuator.nviValue,
        enrollment=pylon.device.isi.Enrollment(
            direction=pylon.device.isi.IsiDirection.INPUT,
            type_id=actuator.nviValue
        )
    )

    #
    #   ISI events
    #
    # noinspection PyUnusedLocal
    def on_user_interface(sender, argument):
        parameter = argument.parameter
        category = pylon.device.isi.IsiEvent.category[argument.event_code]

        if category == pylon.device.isi.IsiEventCategory.ENROLLMENT and \
                parameter != pylon.device.isi.NO_ASSEMBLY:
            parameter = pylon.device.isi.Assembly.assemblies[parameter]

        report(
            'ISI User Interface event: {0} {1}, {2}'.format(
                pylon.device.isi.IsiEventCategory.alpha[category],
                pylon.device.isi.IsiEvent.alpha[argument.event_code],
                parameter
            )
        )

    app.isi.OnUserInterface += on_user_interface

    # noinspection PyUnusedLocal
    def on_enrollment(sender, argument):
        if not argument.automatic:
            advert = argument.enrollment
            if advert.direction == pylon.device.isi.IsiDirection.INPUT and \
                    advert.type_id == ols_assembly.enrollment.type_id and \
                    not advert.variant:
                # Accept for the sensor block:
                argument.result = ols_assembly
            elif advert.direction == pylon.device.isi.IsiDirection.OUTPUT and \
                    advert.type_id == ola_assembly.enrollment.type_id and \
                    not advert.variant:
                # Accept for the actuator block:
                argument.result = ola_assembly

    app.isi.OnEnrollment += on_enrollment

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
    #   menu stuff:
    #
    #
    #	Utilities for reading input from the console and executing
    #	commands. Just type a command and hit Enter.
    #
    def kbhit(timeout):
        """
        Similar to kbhit() on Windows platforms. Note this implementation here
        will not work on Windows platforms. On Windows, you'd use kbhit() from
        the MSCRT instead; see the standard Python module 'msvcrt' for more on
        http://docs.python.org/3.3/library/msvcrt.html

        You could use sys.platform to determine the platform and automatically
        do the right thing, if you wanted to support multiple platforms.
        This function returns true if input is waiting on the console, but
        stops waiting for input when the timeout expires.
        """
        i, o, e = select.select([sys.stdin], [], [], timeout)
        return len(i)

    def menu():
        """
        Function to acquire commands from the console, and execute them.
        The call is blocking.
        """
        # noinspection PyUnusedLocal
        def menu_cancel(args):
            app.isi.cancel_enrollment()
            return False

        def menu_create(args):
            app.isi.create_enrollment(int(args[0]))
            return False

        def menu_eval(args):
            """
            eval evaluates Python expressions within a running program.
            For example, type 'eval print(1234)' to print this number on the
            console. You can interface with the pylon Application class using
            the global variable 'app' defined above, and you can use the
            pseudo-protected app._lts to reach the stack adapter class in this
            manner.
            """
            try:
                eval(args)
            finally:
                return False    # Return True to terminate script.

        # noinspection PyUnusedLocal
        def menu_exit(args):
            print('Winding down...')
            return True

        def menu_extend(args):
            app.isi.extend_enrollment(int(args))
            return False

        def menu_isconnected(args):
            print('Assembly {0} is {1}connected'.format(
                args,
                '' if app.isi.is_connected(int(args)) else 'not '
            ))

        def menu_leave(args):
            app.isi.leave_enrollment(int(args))
            return False

        def menu_help(args):
            """
            help shows the available commands.
            """
            if not len(args):
                for k in items:
                    print('{0:12}\t{1}'.format(k, items[k][1]))
            else:
                if args in items:
                    print('{0:12}\t{1}'.format(args, items[args][1]))
                else:
                    print('No such command: {0}'.format(args))
            return False

        def menu_open(args):
            app.isi.open_enrollment(int(args))
            return False

        # noinspection PyUnusedLocal
        def menu_service(args):
            """
            Sends a service message and an ISI DRUM message.
            """
            app.send_service_message()
            app.isi.send_drum()
            return False

        def menu_sense(args):
            """
            Simulates a sensor reading with the value provided with the
            argument. When no argument is given, use zero.
            """
            if len(args):
                sensor.nvoValue.data = float(args)
            else:
                sensor.nvoValue.data = 0
            return False

        # noinspection PyUnusedLocal
        def menu_wink(args):
            """
            Simulate receipt of a Wink message for testing purposes.
            """
            app.OnWink.fire(app, None)
            return False

        #
        #	Menu items dictionary: command -> (handler function, comment)
        #	Handler functions return True to exit the program.
        items = {
            'cancel':  (menu_cancel,   '      Cancel the pending enrollment'),
            'create':  (menu_create,   'id    Create an enrollment'),
            'eval':    (menu_eval, 	   'stmts Evaluate a Python statement'),
            'exit':    (menu_exit, 	   '      Exit the script'),
            'extend':  (menu_extend,   'id    Extend an enrollment'),
            'is_connected': (menu_isconnected,
                             'id    Whether assembly ID is connected'),
            'help':    (menu_help, 	   '      Display this help'),
            'leave':   (menu_leave,    'id    Leave an existing enrollment'),
            'open':    (menu_open,     'id    Open enrollment'),
            'sense':   (menu_sense,    '[v]   Simulate a sensor reading'),
            'service': (menu_service,  '      Send service and DRUM messages'),
            'wink':    (menu_wink,
                        '      Simulate receipt of a Wink message')
        }

        result = False

        try:
            cmd = sys.stdin.readline().strip().split()
            if len(cmd) > 0:
                command = cmd[0].lower()
                if command in items:
                    result = items[command][0](' '.join(cmd[1:]))
                else:
                    print('Not a valid command. Try \'help\'')
        except Exception as e:
            print(e)
        return result

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
            if kbhit(0.005):
                done = menu()
    finally:

        #
        #   Stop pilon
        #
        app.stop()
        print("Good bye.")


if __name__ == '__main__':
    main()
