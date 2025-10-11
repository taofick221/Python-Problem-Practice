# Create a class object
class myclass:
    x=5
p1= myclass()
print(p1.x)




# using __init__ show result output of a student

class student:
    def __init__(self,name,age,result):
          self.name =name
          self.age=age
          self.result=result
    
    def show(self):
         print(f"Name: {self.name}, Age: {self.age}, Result:{self.result}")


p1=student("Taofick",23,"A+")
p2=student("Nahid",24,"A")

print(p1.name)
print(p2.age)
p1.show()
p2.show()
# without str method
print(p1)




# The __str__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



# Create Methods
class student:
   def __init__(self,name,age):
     self.name=name
     self.age=age
    
   def myfunction(self):
    print("My name is " + self.name)


p1 = student("Taofick",36)

p1.myfunction()
