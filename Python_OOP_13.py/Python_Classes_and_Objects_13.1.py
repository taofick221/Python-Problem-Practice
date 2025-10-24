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
    
    


# Create an object of the Person class
person1 = Person("Alice", 30)
print(person1.greet())

person2 = Person("Bob", 25)
print(person2.greet())




# Use the words mysillyobject and abc instead of self

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



# Delete object properties
del person1.age 
print(person1.greet())  # This will raise an AttributeError since age is deleted
print(person2.greet())

# Delete objects
del person2
# print(person2.greet())  # This will raise a NameError since person2 is deleted
# Create a class with a method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
    


