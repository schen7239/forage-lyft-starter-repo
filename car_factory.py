from datetime import date
from car import Car
from battery.model.nubbin_battery import NubbinBattery
from battery.model.spindler_battery import SpindlerBattery
from engine.engine_model.capulet_engine import CapuletEngine
from engine.engine_model.sternman_engine import SternmanEngine
from engine.engine_model.willoughby_engine import WilloughbyEngine

class CarFactory():
    def __init__(self):
        pass
        
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery=battery, engine=engine)
    
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery=battery, engine=engine)
    
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool = False) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery=battery, engine=engine)
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(battery=battery, engine=engine)
    
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(battery=battery, engine=engine)
