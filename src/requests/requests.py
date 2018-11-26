class Request:
    """Handles parking lot commands."""

    @classmethod
    def handle_request(cls, command):
        print 'Handling command: ', command
