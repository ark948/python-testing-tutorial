import random
import unittest
from unittest.mock import MagicMock, patch

# sensory.py
class Sensor:
    @property
    def temperature(self):
        return random.randint(10, 45)
    

# alarm.py    
class Alarm:
    def __init__(self, sensor=None) -> None:
        self._low = 18
        self._high = 24
        self._sensor = sensor or Sensor()
        self._is_on = False

    def check(self):
        temperature = self._sensor.temperature
        if temperature < self._low or temperature > self._high:
            self._is_on = True

    @property
    def is_on(self):
        return self._is_on
    
# test_sensor.py
class TestSensor: # thsi is a stub for Sensor class
    def __init__(self, temperature) -> None:
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature
    
# test_alarm.py
class TestAlarm(unittest.TestCase):
    def test_is_alarm_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_on)

    def test_check_temperature_too_high(self):
        alarm = Alarm(TestSensor(25))
        alarm.check()
        self.assertTrue(alarm.is_on)

    def test_check_temperature_too_low(self):
        alarm = Alarm(TestSensor(17))
        alarm.check()
        self.assertTrue(alarm.is_on)

    def test_check_normal_temperature(self):
        alarm = Alarm(TestSensor(20))
        alarm.check()
        self.assertFalse(alarm.is_on)

# creating stubs using MagicMock
# instead of creating an instance of alarm in everymethod
# setUp will be used
class TestAlarmByMagicMock(unittest.TestCase):
    def setUp(self):
        self.mock_sensor = MagicMock(Sensor)
        self.alarm = Alarm(self.mock_sensor)

    def test_is_alarm_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_on)

    def test_check_temperature_too_high(self):
        self.mock_sensor.temperature = 25
        self.alarm.check()
        self.assertTrue(self.alarm.is_on)

    def test_check_temperature_too_low(self):
        self.mock_sensor.temperature = 15
        self.alarm.check()
        self.assertTrue(self.alarm.is_on)

    def test_check_normal_temperature(self):
        self.mock_sensor.temperature = 20
        self.alarm.check()
        self.assertFalse(self.alarm.is_on)
        
# This one fails, no idea how to fix it
class TestAlarm3(unittest.TestCase):
    @patch('sensor.Sensor')
    def test_check_temperature_too_low_patched(self, sensor):
        sensor.temperature = 10
        alarm = Alarm(sensor)
        alarm.check()
        self.assertTrue(alarm.is_on)


if __name__ == "__main__":
    unittest.main(verbosity=2)