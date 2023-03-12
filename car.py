from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, battery: Battery, engine: Engine) -> None:
        super().__init__()
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.battery_should_be_serviced() or self.engine.engine_should_be_serviced()
