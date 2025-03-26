#Inheritance 👨‍👩‍👧‍👦: 
# Just like humans inherit traits from their parents,
#  classes can inherit attributes and methods from other classes.
#  This helps reduce code repetition and create a natural hierarchy in your code!

class Vehicle:
    def __init__(self,wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)