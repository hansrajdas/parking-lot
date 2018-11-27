import utils

class Request:
    """Handles parking lot commands."""

    @classmethod
    def handle_request(cls, command):
        utils.console_log(command)
