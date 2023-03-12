import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        
        car_factory = CarFactory()
        Calliope = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Calliope.needs_service())