import utils

from parking.parking_spot import ParkingSpot
from parking.vehicle import Vehicle
from storage.min_heap import MinHeap

class ParkingLot:
    """Manages parking lot."""
    def __init__(self, number_of_slots):
        self.free_slots = number_of_slots
        self.slots = MinHeap(number_of_slots)
        self.vehicles = {}  # Maps parking spot to vehicle
        utils.console_log(
            'Created a parking lot with %d slots' % number_of_slots)

    def _get_next_free_slot(self):
        return self.slots.extract_min(self.free_slots)

    def park_vehicle(self, registration_number, color):
        if not self.free_slots:
            utils.console_log('Sorry, parking lot is full')
            return None
        spot = self._get_next_free_slot()
        self.vehicles[spot.spot_num] = Vehicle(registration_number, color)
        self.free_slots -= 1
        utils.console_log('Allocated slot number: %d' % spot.spot_num)

    def free_parking_spot(self, spot_num):
        """Frees a given parking spot."""
        pass

    def get_parking_status(self):
        """Prints detail of all vehicles present in parking lot."""
        pass

    def get_registration_numbers_with_color(self, color):
        """Prints list of registration numbers with given vehicle color."""
        pass

    def get_slot_numbers_with_color(self, color):
        """Prints list of slot numbers with given vehicle color."""
        pass

    def get_slot_num_with_vehicle_reg_num(self, registration_num):
        """
        Prints slot number where vehicle with given registration number is
        parked.
        """
        pass
