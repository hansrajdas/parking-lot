class ParkingSpot:
    def __init__(self, spot_num):
        self.spot_num = spot_num
        self.vehicle = None

    def get_spot_num(self):
        return self.spot_num

    def get_vehicle_parked(self):
        """Returns the details of vehicle parked at this spot."""
        return self.vehicle

    def set_spot(self, vehicle):
        """Parks a vehicle at this spot."""
        self.vehicle = vehicle
