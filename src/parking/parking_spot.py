class ParkingSpot:
    """Holds parking spot attributes."""
    def __init__(self, spot_id):
        self.id = spot_id
        # We can further attributes like size of this spot.
        # self.size = size

    def get_spot_num(self):
        return self.id
