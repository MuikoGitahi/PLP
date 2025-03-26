# Parent class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")

# Child class (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.__file_size = file_size  # Private attribute (Encapsulation)

    def read(self):
        print(f"You open the eBook '{self.title}' on your device.")

    def get_file_size(self):  # Getter method for encapsulation
        return f"The file size of '{self.title}' is {self.__file_size}MB."

# Creating objects
physical_book = Book("Harry Potter", "J.K. Rowling", 350)
ebook = EBook("Python Basics", "John Doe", 200, 2)

# Using the read() method (demonstrates polymorphism)
physical_book.read()  # Output: You start reading 'Harry Potter' by J.K. Rowling.
ebook.read()          # Output: You open the eBook 'Python Basics' on your device.

# Accessing encapsulated attribute using getter method
print(ebook.get_file_size())  # Output: The file size of 'Python Basics' is 2MB.



        