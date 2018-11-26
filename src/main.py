#!/usr/bin/python

import interface
import sys

def usage(argument_list):
    print 'Invalid arguments received!'
    print 'Usage: bin/parking_lot <commands_file.txt>'


def main():
    """Starting point of parking lot application."""
    if len(sys.argv) != 2:
        usage(sys.argv)
        sys.exit(1)

    # Launch application
    try:
        interface.parse_and_process_requests(sys.argv[1])
    except IOError, msg:
        print msg


if __name__ == '__main__':
    main()
