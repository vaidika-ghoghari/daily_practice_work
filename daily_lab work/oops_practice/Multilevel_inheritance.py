#Multilevel Inheritance

#When a class inherits from another class, and a third class inherits from that child class,
#   it is called multilevel inheritance.

class Vehical :

    def __init__(self, brand ,model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand}  {self.model} has started . ")


class Car(Vehical):

    def __init__(self , brand ,model , fuel_type):
        super().__init__(brand , model)
        self.fuel_type = fuel_type

    def fuel_info(self):
        print(f"{self.fuel_type}")

class ElectricCar(Car):

    def __init__(self, brand ,model ,bettery_capacity ):
        super().__init__(brand ,model ,fuel_type = "Electricity")
        self.bettery_capacity = bettery_capacity

    def charge_info(self):
        print(f"Bettery Capacity : {self.bettery_capacity}")

ev = ElectricCar("Tata" ,"Nexon EV" , 40)
ev.start()
ev.fuel_info()
ev.charge_info()
