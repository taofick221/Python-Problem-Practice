class Vehicale:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Good")

class car(Vehicale):
    def move(self):
         print("nothing")

class boat(Vehicale):
        def move(self):
             print("no")

class bus(Vehicale):
     def move(self):
          print("color")

car1=car("bmw",2000)
boat1=boat("DVE",2020)
bus1=bus("volvo",2024)

for x in (car1,boat1,bus1):
     print(x.brand)
     print(x.model)
     x.move()

