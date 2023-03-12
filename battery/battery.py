from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    @abstractmethod
    def battery_should_be_serviced() -> bool:
        pass