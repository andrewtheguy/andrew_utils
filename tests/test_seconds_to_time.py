
import unittest

from andrew_utils import seconds_to_time


class TestSecondsToTime(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(seconds_to_time(0), "00:00:00.000")

    def test_regular(self):
        self.assertEqual(seconds_to_time(50.123), "00:00:50.123")

    def test_regular_with_minutes(self):
        self.assertEqual(seconds_to_time(110.123), "00:01:50.123")

    def test_regular_with_hours(self):
        self.assertEqual(seconds_to_time(3710.123), "01:01:50.123")

    def test_regular_with_day(self):
        self.assertEqual(seconds_to_time(86510.987), "24:01:50.987")

    def test_no_unneeded_rounding(self):
        self.assertEqual(seconds_to_time(59.999), "00:00:59.999")
        self.assertEqual(seconds_to_time(3599.999), "00:59:59.999")

    def test_rounding_to_minutes(self):
        self.assertEqual(seconds_to_time(59.9999), "00:01:00.000")
        self.assertEqual(seconds_to_time(119.9999), "00:02:00.000")

    def test_rounding_to_hours(self):
        self.assertEqual(seconds_to_time(3599.9999), "01:00:00.000")
        self.assertEqual(seconds_to_time(7199.9999), "02:00:00.000")


    def test_zero_no_decimal(self):
        self.assertEqual(seconds_to_time(0,include_decimals=False), "00:00:00")

    def test_regular_no_decimal(self):
        self.assertEqual(seconds_to_time(62,include_decimals=False), "00:01:02")

    def test_hours_no_decimal_round_down(self):
        self.assertEqual(seconds_to_time(3710.1234,include_decimals=False), "01:01:50")

    def test_hours_no_decimal_round_up(self):
        self.assertEqual(seconds_to_time(3710.987654,include_decimals=False), "01:01:51")

    def test_hours_no_decimal_round_up_to_minute(self):
        self.assertEqual(seconds_to_time(59.987,include_decimals=False), "00:01:00")
        self.assertEqual(seconds_to_time(119.987,include_decimals=False), "00:02:00")


    def test_hours_no_decimal_round_up_to_hour(self):
        self.assertEqual(seconds_to_time(3599.987,include_decimals=False), "01:00:00")
        self.assertEqual(seconds_to_time(7199.987,include_decimals=False), "02:00:00")

    def test_day_no_decimal(self):
        self.assertEqual(seconds_to_time(86510.1234,include_decimals=False), "24:01:50")
