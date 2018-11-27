#!/usr/bin/python

import interface
import sys
import utils


def main():
    """Starting point of parking lot application."""
    if len(sys.argv) == 2:
        try:
            interface.read_commands_from_file(sys.argv[1])
        except IOError, msg:
            utils.console_log(msg)
    elif len(sys.argv) == 1:
        interface.launch_interactive_mode()
    else:
        usage(sys.argv)
        utils.exit_app(1)


if __name__ == '__main__':
    main()
