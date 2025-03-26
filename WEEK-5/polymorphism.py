#Polymorphism 🦄:
# Derived classes can behave differently for the same method inherited from a base class. 
# With polymorphism, a method name can mean different things across multiple classes.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())