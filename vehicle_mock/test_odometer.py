import unittest
from unittest.mock import Mock
import odometer

class TestOdometer(unittest.TestCase):
    def test_alert_normal(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 70
        # 70 is normal, do not raise alarm -> alarm is false
        self.assertFalse(odometer.alert())

    def test_alert_overspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 100
        # 100 is normal, do not raise alarm -> alarm is false
        self.assertFalse(odometer.alert())

    def test_alert_underspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 59
        # 59 is below 60, not normal, raise alarm -> arlam is true
        self.assertTrue(odometer.alert())

if __name__ == "__main__":
    unittest.main(verbosity=2)