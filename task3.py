class vehicle:
    def __init__(self, vehicle_type,):
        self.vehicle_type = vehicle_type
        
    def start(self):
        print(f"vehicle_type: {self.vehicle_type}")
        
        
class car(vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors 
    
    def shut(self):
        super().start()
        print(f"number_of_doors: {self.number_of_doors}")
        
        
class Electric_car(car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity
    def battery(self):
        super().shut()
        print(f"battery_capacity: {self.battery_capacity}")
        
        
Electric_car1=Electric_car("V8", 6, "400000mvh") 
Electric_car1.battery()          
        
