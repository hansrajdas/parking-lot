import utils

from commands.parser import ParserAndValidateCommand
from requests.requests import Request

def read_commands_from_file(filename):
    """Read commands from file and sends for processing."""
    file_fp = open(filename, 'r')
    command = file_fp.readline()
    while command:
        parse_and_process_command(command)
        command = file_fp.readline()
    file_fp.close()

def launch_interactive_mode():
    """Keeps on reading commands from console until exit command."""
    while True:
        command = raw_input().strip()
        parse_and_process_command(command)

def parse_and_process_command(command):
    """Parses raw command and if command is valid, executes it."""
    parsed_command = ParserAndValidateCommand.parse_command(command)
    if parsed_command:
        Request.handle_request(parsed_command)
