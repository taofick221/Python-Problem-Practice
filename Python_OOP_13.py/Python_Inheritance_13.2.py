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

p1=student("Taofick","Mahmoodur Rahaman")
p1.printname()
print(f"Age: {p1.age}")


