# Create a class 
class MyClass:
    x = 5

# Create an object of the class
my_object = MyClass()

# Access the class variable
print(my_object.x)

# Create a class with an __init__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    