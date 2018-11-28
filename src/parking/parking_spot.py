class ParkingSpot:
    def __init__(self, spot_id):
        self.id = spot_id
        self.vehicle = None

    def get_spot_num(self):
        return self.id

    def get_vehicle_parked(self):
        """Returns the details of vehicle parked at this spot."""
        return self.vehicle

    def set_spot(self, vehicle):
        """Parks a vehicle at this spot."""
        self.vehicle = vehicle
