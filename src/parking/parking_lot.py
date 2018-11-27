class ParkingLot:
    """Manages parking lot."""
    def __init__(self, number_of_slots):
        self.total_slots = number_of_slots
        self.free_slots = [i + 1 for i in range(number_of_slots)]

    def get_next_free_slot(self):
        pass
