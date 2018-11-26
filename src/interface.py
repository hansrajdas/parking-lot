def parse_and_process_requests(filename):
    """Read commands from file and sends for processing."""
    file_fp = open(filename, 'r')
    command = file_fp.readline()
    while command:
        print command
        command = file_fp.readline()
    file_fp.close()
