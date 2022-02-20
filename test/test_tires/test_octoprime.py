import unittest

from tires.OctoprimeTires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1,1,1,1]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())
    def test_needs_service_false(self):
        tire_wear = [0,0,0.3,0.3,0.3]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service)
