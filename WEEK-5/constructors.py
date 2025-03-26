#What’s a Constructor? 
# Every time you create a new object, you want it to have its unique attributes (color, model, etc.). 
# Constructors (__init__ methods) allow each object to start with specific values

#Instance Variables
#Instance variables are specific to each object and can vary across objects. 
# For example, two Car objects can have different colors, models, and speeds.

#Example: Setting Up Your Constructor!

class Car:
    def __init__(self, color, model):
        self.color = color  #An Instance Variable
        self.model = model  #An Instance Variable

#Creating 2 objects with unique attributes
car1 = Car("Black", "Mercides")
car2 = Car("Red", "Tesla")

print(car1.color)
print(car2.model)
