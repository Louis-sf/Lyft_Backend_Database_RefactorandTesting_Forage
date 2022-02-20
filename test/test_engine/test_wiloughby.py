import unittest

from engine.willoughby_engine import Willoughby


class TesWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 99999999
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 1
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())