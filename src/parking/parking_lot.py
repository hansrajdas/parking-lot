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
        """Returns next free slot - having min slot number."""
        return self.slots.extract_min(self.free_slots)

    def _add_to_free_slots(self, spot_num):
        """Adds given slot back to pool of free slots."""
        self.slots.add_to_heap(self.free_slots, spot_num)

    def park_vehicle(self, registration_number, color):
        if not self.free_slots:
            utils.console_log('Sorry, parking lot is full')
            return None
        spot = self._get_next_free_slot()
        self.vehicles[spot.id] = Vehicle(registration_number, color)
        self.free_slots -= 1
        utils.console_log('Allocated slot number: %d' % spot.id)

    def free_parking_spot(self, spot_num):
        """Frees a given parking spot."""
        if spot_num not in self.vehicles:
            utils.console_log('Parking spot[%d] is already free' % spot_num)
            return None
        del self.vehicles[spot_num]
        self._add_to_free_slots(spot_num)
        self.free_slots += 1
        utils.console_log('Slot number %d is free' % spot_num)

    def get_parking_status(self):
        """Prints detail of all vehicles present in parking lot."""
        data = [('Slot No.', 'Registration No', 'Colour')]
        for slot_num in sorted(self.vehicles):
            vehicle = self.vehicles[slot_num]
            data.append((slot_num, vehicle.registration_num, vehicle.color))
        utils.print_table(data)

    def get_registration_numbers_with_color(self, color):
        """Prints list of registration numbers with given vehicle color."""
        registration_nums = [
            self.vehicles[spot].registration_num for spot in self.vehicles
            if self.vehicles[spot].color == color
        ]
        utils.console_log(', '.join(registration_nums))

    def get_slot_numbers_with_color(self, color):
        """Prints list of slot numbers with given vehicle color."""
        spot_numbers = [
            str(spot) for spot in self.vehicles
            if self.vehicles[spot].color == color
        ]
        utils.console_log(', '.join(spot_numbers))

    def get_slot_num_with_vehicle_reg_num(self, registration_num):
        """
        Prints slot number where vehicle with given registration number is
        parked.
        """
        for slot_num in self.vehicles:
            if self.vehicles[slot_num].registration_num == registration_num:
                utils.console_log(str(slot_num))
                return None
        utils.console_log('Not found')
