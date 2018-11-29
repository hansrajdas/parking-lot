import utils

# Map of all supported commands and number of arguments required for that
# command.
SUPPORTED_COMMANDS = {
    'create_parking_lot': 1,
    'park': 2,
    'leave': 1,
    'status': 0,
    'registration_numbers_for_cars_with_colour': 1,
    'slot_numbers_for_cars_with_colour': 1,
    'slot_number_for_registration_number': 1,
    'exit': 0,
}


class ParserAndValidateCommand:
    """Parses parking lot commands."""

    @classmethod
    def parse_command(cls, command):
        """Parses given command."""
        if not command:
            return False
        return cls.validate_command(command.strip().split(' '))

    @classmethod
    def validate_command(cls, command):
        """Validates if command is valid or not."""
        if command[0] not in SUPPORTED_COMMANDS:
            utils.console_log('%s: command not found' % command[0])
            return False
        elif SUPPORTED_COMMANDS[command[0]] != len(command) - 1:
            utils.console_log('%s: invalid number of arguments' % (command[0]))
            return False
        return command
