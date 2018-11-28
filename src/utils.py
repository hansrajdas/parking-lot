"""This file contains utility functions."""

import sys


def console_log(message):
    print(message)


def exit_app(status):
    sys.exit(status)


def usage():
    console_log('Invalid arguments received!')
    console_log('Usage: bin/parking_lot <command_file.txt> OR bin/parking_lot')


def print_table(matrix):
    """Prints MxN matrix in tabular format."""
    for row in matrix:
        data = []
        for val in row:
            data.append('%-18s' % str(val))  # Each column is 18 chars long
        console_log(''.join(data))
