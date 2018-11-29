"""Contains unit test cases for handler module."""

import mock
import os
import sys
import unittest

sys.path.append(os.path.abspath(__file__ + "/../.."))

import utils

from handlers.handler import Handler


class HandlerTest(unittest.TestCase):
    """Unit tests for handler module."""

    def tearDown(self):
        """Resets parking lot after executing each test case."""
        Handler.parking_lot = None

    def test_handle_request_create_parking_lot(self):
        """Verify that parking lot created."""
        # Initially parking lot must be None
        self.assertIsNone(Handler.parking_lot)
        Handler.handle_request(['create_parking_lot', 2])

        # Now parking lot is created, parking_lot must have some reference.
        self.assertIsNotNone(Handler.parking_lot)

    @mock.patch.object(utils, 'exit_app')
    def test_handle_request_exit(self, mocked_exit_app):
        """Verifies that exit command calls exit_app utility function."""
        Handler.handle_request(['exit'])
        mocked_exit_app.assert_called_with(0)

    @mock.patch.object(utils, 'console_log')
    def test_handle_request_command_not_found(self, mocked_console_log):
        """Verifies that error message is shown if command is not found."""
        Handler.handle_request(['create_parking_lot', 1])
        Handler.handle_request(['parking'])
        mocked_console_log.assert_called_with('parking: command not found')

    @mock.patch.object(utils, 'console_log')
    def test_handle_request_is_parking_lot_created(self, mocked_console_log):
        """
        Verifies that before creating parking lot, we can't do any other
        operation.
        """
        # We can't park vehicle before creating a parking lot.
        Handler.handle_request(['park', 'number', 'color'])
        mocked_console_log.assert_called_with(
                'please create parking lot before this operation')

        # We can't leave a spot before creating a parking lot.
        Handler.handle_request(['leave', 1])
        mocked_console_log.assert_called_with(
                'please create parking lot before this operation')


if __name__ == '__main__':
    unittest.main()
