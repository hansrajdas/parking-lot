import utils

from parking.parking_lot import ParkingLot


class Handler:
    """Handles parking lot commands."""

    parking_lot = None

    @classmethod
    def handle_request(cls, command):
        """Handles command request and invokes required parking lot method."""
        command_name = command[0]
        if command_name == 'create_parking_lot':
            Handler.parking_lot = ParkingLot(int(command[1]))
        elif command_name == 'exit':
            utils.exit_app(0)
        elif not Handler.parking_lot:
            utils.console_log(
                'please create parking lot before this operation')
        elif command_name == 'park':
            Handler.parking_lot.park_vehicle(command[1], command[2])
        elif command_name == 'leave':
            Handler.parking_lot.free_parking_spot(int(command[1]))
        elif command_name == 'status':
            Handler.parking_lot.get_parking_status()
        elif command_name == 'registration_numbers_for_cars_with_colour':
            Handler.parking_lot.get_registration_numbers_with_color(command[1])
        elif command_name == 'slot_numbers_for_cars_with_colour':
            Handler.parking_lot.get_slot_numbers_with_color(command[1])
        elif command_name == 'slot_number_for_registration_number':
            Handler.parking_lot.get_slot_num_with_vehicle_reg_num(command[1])
        else:
            utils.console_log('%s: command not found' % command_name)
