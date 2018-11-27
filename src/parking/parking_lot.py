import utils

from parking.parking_spot import ParkingSpot

class ParkingLot:
    """Manages parking lot."""
    def __init__(self, number_of_slots):
        self.total_slots = number_of_slots
        self.free_slots = [ParkingSpot(i + 1) for i in range(number_of_slots)]
        self.vehicles = {}  # Maps parking spot to vehicle
        utils.console_log(
            'Created a parking lot with %d slots\n' % number_of_slots)

    def get_next_free_slot(self):
        pass
