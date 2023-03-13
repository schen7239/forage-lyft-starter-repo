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
        self.assertTrue(Calliope.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        
        car_factory = CarFactory()
        Calliope = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Calliope.needs_service())
        
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        Calliope = car_factory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        car_factory = CarFactory()
        Calliope = car_factory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Calliope.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        Glissade = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        Glissade = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Glissade.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_factory = CarFactory()
        Glissade = car_factory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        car_factory = CarFactory()
        Glissade = car_factory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Glissade.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        car_factory = CarFactory()
        Palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(Palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        car_factory = CarFactory()
        Palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(Palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car_factory = CarFactory()
        Palindrome = car_factory.create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertTrue(Palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car_factory = CarFactory()
        Palindrome = car_factory.create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertFalse(Palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        Rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        Rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_factory = CarFactory()
        Rorschach = car_factory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_factory = CarFactory()
        Rorschach = car_factory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Rorschach.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        Thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        Thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        
        self.assertFalse(Thovex.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        Thovex = car_factory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        car_factory = CarFactory()
        Thovex = car_factory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Thovex.needs_service())
        
if __name__ == '__main__':
    unittest.main()