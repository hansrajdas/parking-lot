from commands.parser import Parser

def read_commands(filename):
    """Read commands from file and sends for processing."""
    file_fp = open(filename, 'r')
    command = file_fp.readline()
    while command:
        print command
        Parser.handle_request(command)
        command = file_fp.readline()
    file_fp.close()
