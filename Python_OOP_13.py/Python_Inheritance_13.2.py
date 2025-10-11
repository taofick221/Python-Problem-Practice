# Use the Student class to create an object, and then execute the printname method:
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        print(f"Name: {self.firstname} {self.lastname}")
    
class student(person):
    pass

p1=student("Taofick","Mahmoodur Rahaman")
p1.printname()






# override a parent class 
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        print(f"Name: {self.firstname} {self.lastname}")
    
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.age=28
    
    def welcome(self):
        print(f"Welcome to our university {self.firstname} {self.lastname}({self.age})")

p1=student("Taofick","Mahmoodur Rahaman")
p1.printname()
print(f"Age: {p1.age}")
p1.welcome()







# Problem: Employee Management
# You need to make two classes — Employee (parent) and Manager (child).
class Employee:
    def __init__(self,name,salary):
        self.firstname=name
        self.salary=salary

    def showInfo(self):
        print(f"Name: {self.firstname}")
        print(f"Salary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def showInfo(self):
        print(f"Name: {self.firstname}")
        print(f"Salary: {self.salary}")   
        print(f"Department: {self.department}")

Manager =Manager("Taofick",25000,"IT")
Manager.showInfo()
