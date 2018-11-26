SUPPORTED_COMMANDS = {
    'create_parking_lot': 1,
    'park': 2,
    'leave': 1,
    'status': 0,
    'registration_numbers_for_cars_with_colour': 1,
    'slot_numbers_for_cars_with_colour': 1,
    'slot_number_for_registration_number': 1,
}

class Parser:
    """Parses parking lot commands."""

    def parse_command(self, command):
        """Parses given command."""
        if not command:
            print '[Error]: Empty command received'
            return False
        return self.validate_command(command.strip().split(' '))

    def validate_command(self, command):
        """Validates if command is valid or not."""
        if command[0] not in SUPPORTED_COMMANDS:
            print '[Error]: Command not supported - %s' % command[0]
            return False
        elif SUPPORTED_COMMANDS[command[0]] != len(command) - 1:
            print '[Error]: Invalid number of arguments for command: %s' % (
            command[0])
            return False
        return command
