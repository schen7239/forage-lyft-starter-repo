from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def engine_should_be_serviced():
        pass
    
    