class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        return(f"brand: {self.brand}, model: {self.model}")

#dev = Device("apple", "iphone 14") 
#print(dev.display_info())   
        
class smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity
        
    def show_info(self):
        
        print(super().show_info(), f"storage capacity: {self.storage_capacity} GB") 
        
Device1=smartphone("Apple", "Iphone 14", 128)
Device1.show_info()      