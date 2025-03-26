#Create a program that includes animals or vehicles with the same action (like move()).
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky.")

# Using polymorphism
animals = [Dog(), Bird()]

for animal in animals:
    animal.move()
