class Vehicle:
    def max_speed(self):
        pass
class Car(Vehicle):
    def max_speed(self):
        return "max speed 270 kmph"
class Truck(Vehicle):
    def max_speed(self):
        return "max speed 120 kmph"
class Motorcycle(Vehicle):
    def max_speed(self):
        return "max speed 320"
vehicles=[Car(), Truck(), Motorcycle()]
for n in vehicles:
    print(n.max_speed())