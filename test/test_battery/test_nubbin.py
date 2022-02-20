import unittest
from datetime import date

from battery.nubbin import Nubbin

class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-02-01")
        last_service_date = date.fromisoformat("1999-07-18")
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-02-01")
        last_service_date = date.fromisoformat("2021-07-18")
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())