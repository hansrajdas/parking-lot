# This file contains utility functions.

import sys


def console_log(message):
    print (message)

def exit_app(status):
    sys.exit(status)

def usage():
    console_log('Invalid arguments received!')
    console_log('Usage: bin/parking_lot <commands_file.txt> OR bin/parking_lot')
