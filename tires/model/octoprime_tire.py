from ..tires import Tire

class OctoprimeTire(Tire):
    def __init__(self):
        super().__init__()
    
    def tires_should_be_serviced(self):
        if sum(self.tire_wear) >= 3:
            return False
        return True
    
