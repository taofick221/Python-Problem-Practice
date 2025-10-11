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

p1=student("Taofick",23,"A+")
p2=student("Nahid",24,"A")

print(p1.name)
print(p2.age)
