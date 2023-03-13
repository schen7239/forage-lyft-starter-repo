from ..tires import Tire

class CarriganTire(Tire):
    def __init__(self):
        super().__init__()
    
    def tires_should_be_serviced(self):
        for count, ele in enumerate(self.tire_wear):
            if ele < .9:
                return True
        return True
    
