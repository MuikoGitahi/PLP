#What’s a Constructor? 
# Every time you create a new object, you want it to have its unique attributes (color, model, etc.). 
# Constructors (__init__ methods) allow each object to start with specific values

#Instance Variables
#Instance variables are specific to each object and can vary across objects. 
# For example, two Car objects can have different colors, models, and speeds.

#Example: Setting Up Your Constructor!

class Car:
    def __init__(self, color, model, top_speed):
       self.color = color
       self.model = model
       self.top_speed = top_speed
   

#Creating 2 objects with unique attributes
car1 = Car(color="Black", model="Mercedes", top_speed=220)
car2 = Car(color="White",model="Dodge", top_speed=300)

print(car1.model)
print(car1.top_speed)
print(car1.color)
print(car2.model)
print(car2.color)
print(car2.top_speed)
 