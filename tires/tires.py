from abc import ABC, abstractmethod
import random

class Tire(ABC):
    def __init__(self) -> None:
        self.tire_wear = [random.random() for _ in range(4)]
    
    @abstractmethod
    def tires_should_be_serviced(self) -> bool:
        pass
    