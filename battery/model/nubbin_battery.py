from battery.battery import Battery
from abc import ABC
from datetime import datetime, timedelta

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
        
    def battery_should_be_serviced(self) -> bool:
        return self.current_date > self.last_service_date + timedelta(years = 4)