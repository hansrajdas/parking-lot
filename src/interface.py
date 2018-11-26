from commands.parser import Parser
from requests.requests import Request

def read_commands(filename):
    """Read commands from file and sends for processing."""
    file_fp = open(filename, 'r')
    command = file_fp.readline()
    while command:
        parsed_command = Parser.parse_command(command)
        if parsed_command:
            Request.handle_request(parsed_command)
        command = file_fp.readline()
    file_fp.close()
