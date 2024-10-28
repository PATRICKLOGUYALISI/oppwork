class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        
    def show_details(self):
        print(f"brand: {self.brand}, power: {self.power}")    


class WashingMachine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size
        
    def show_details(self):
        super().show_details()
        print(f"drum_size: {self.drum_size}")
        
washingMachine=WashingMachine("LG", 800000, "small")
washingMachine.show_details()            
        
        
        
        
    