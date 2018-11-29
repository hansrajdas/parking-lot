"""Contains unit test cases for parking_lot module."""

import sys
import os
import unittest

sys.path.append(os.path.abspath(__file__ + "/../.."))

import utils

from parking.parking_lot import ParkingLot
import mock


class ParkingLotTest(unittest.TestCase):
    """Unit tests for parking lot module."""

    @mock.patch.object(utils, 'console_log')
    def test_park_vehicle(self, mocked_log_fn):
        """Verify that first free parking spot is given to new vehicle."""
        self.parking_lot = ParkingLot(3)

        self.parking_lot.park_vehicle('DL-1234', 'Blue')
        mocked_log_fn.assert_called_with('Allocated slot number: 1')

        self.parking_lot.park_vehicle('DL-1235', 'White')
        mocked_log_fn.assert_called_with('Allocated slot number: 2')

    @mock.patch.object(utils, 'console_log')
    def test_park_vehicle_parking_full(self, mocked_log_fn):
        """Verify that parking full message is printed, when all allocated."""
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-1', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-2', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-3', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-4', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-5', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-6', 'Blue')
        mocked_log_fn.assert_called_with('Sorry, parking lot is full')

    def test_free_parking_lot(self):
        """Verifies that a parking slot is freed and spot is back to pool."""
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-1', 'Blue')
        self.assertEqual(self.parking_lot.free_slots, 4)

        self.parking_lot.free_parking_spot(1)
        # After freeing slot 1, free slots count should be back to 5.
        self.assertEqual(self.parking_lot.free_slots, 5)

    @mock.patch.object(utils, 'console_log')
    def test_free_parking_lot_error(self, mocked_log_fn):
        """
        Verifies that required message is printed if spot is already free and
        that spot is attempted to be freed.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.free_parking_spot(1)
        mocked_log_fn.assert_called_with('Parking spot[1] is already free')

    @mock.patch.object(utils, 'print_table')
    def test_get_parking_status(self, mocked_print_table):
        """
        Verifies that status command prints all vehicle information in sorted
        order.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-1', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-2', 'Black')
        self.parking_lot.park_vehicle('DL-TEST-3', 'White')
        expected_table = [
            ('Slot No.', 'Registration No', 'Colour'),
            (1, 'DL-TEST-1', 'Blue'),
            (2, 'DL-TEST-2', 'Black'),
            (3, 'DL-TEST-3', 'White'),
        ]
        self.parking_lot.get_parking_status()
        mocked_print_table.assert_called_with(expected_table)

    @mock.patch.object(utils, 'console_log')
    def test_get_registration_numbers_with_color(self, mocked_log_fn):
        """
        Verifies that correct registration number is fetched having given
        color.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-Blue', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-Black', 'Black')
        self.parking_lot.park_vehicle('DL-TEST-White', 'White')

        self.parking_lot.get_registration_numbers_with_color('White')
        mocked_log_fn.assert_called_with('DL-TEST-White')

    @mock.patch.object(utils, 'console_log')
    def test_get_slot_numbers_with_color(self, mocked_log_fn):
        """
        Verifies that correct parking spot number is fetched having given
        color.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-Blue', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-Black', 'Black')
        self.parking_lot.park_vehicle('DL-TEST-White', 'White')

        self.parking_lot.get_slot_numbers_with_color('Black')
        mocked_log_fn.assert_called_with('2')

    @mock.patch.object(utils, 'console_log')
    def test_get_slot_num_with_vehicle_reg_num(self, mocked_log_fn):
        """
        Verifies that correct parking spot number is fetched with given
        registration number.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-Blue', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-Black', 'Black')
        self.parking_lot.park_vehicle('DL-TEST-White', 'White')

        self.parking_lot.get_slot_num_with_vehicle_reg_num('DL-TEST-Black')
        mocked_log_fn.assert_called_with('2')

    @mock.patch.object(utils, 'console_log')
    def test_get_slot_num_with_vehicle_reg_num_not_found(self, mocked_log_fn):
        """
        Verifies that error message is printed if registration number is not
        found in parking lot.
        """
        self.parking_lot = ParkingLot(5)
        self.parking_lot.park_vehicle('DL-TEST-Blue', 'Blue')
        self.parking_lot.park_vehicle('DL-TEST-White', 'White')

        self.parking_lot.get_slot_num_with_vehicle_reg_num('DL-TEST-Black')
        mocked_log_fn.assert_called_with('Not found')


if __name__ == '__main__':
    unittest.main()
