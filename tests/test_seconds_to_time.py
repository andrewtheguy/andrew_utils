
import unittest

from andrew_utils import seconds_to_time


class TestSecondsToTime(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(seconds_to_time(0), "00:00:00.000000")

    def test_regular(self):
        self.assertEqual(seconds_to_time(50.123456), "00:00:50.123456")

    def test_regular_with_minutes(self):
        self.assertEqual(seconds_to_time(110.123456), "00:01:50.123456")

    def test_regular_with_hours(self):
        self.assertEqual(seconds_to_time(3710.123456), "01:01:50.123456")

    def test_regular_with_day(self):
        self.assertEqual(seconds_to_time(86510.987654), "24:01:50.987654")


    def test_regular_no_decimal(self):
        self.assertEqual(seconds_to_time(0,include_decimals=False), "00:00:00")

    def test_hours_no_decimal(self):
        self.assertEqual(seconds_to_time(3710.987654,include_decimals=False), "01:01:50")

    def test_day_no_decimal(self):
        self.assertEqual(seconds_to_time(86510.987654,include_decimals=False), "24:01:50")
