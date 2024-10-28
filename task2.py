class camera:
    def take_photo(self):
        print("take photo")

class phone:
    def make_call(self):
        print("making a phone call....")
        
class smartphone(camera, phone):
    pass

smartphone = smartphone()


smartphone.take_photo()
smartphone.make_call()        