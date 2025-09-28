# Creating a function
def my_function():
    print("Hello from a function")



# Calling a function
def my_function():
    print("Hello from a function")
my_function()


# Function with parameters
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")   
my_function("Linus")



# Function with multiple parameters
def my_function(fname, lname):
    print(fname + " " + lname)  
my_function("Emil", "Refsnes")
my_function("Tobias", "Refsnes")
my_function("Linus", "Refsnes")
print()


# Function with default parameter values
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




# Function with return value
def my_function(x):
    return 5 * x    
print(my_function(3))

print(my_function(5))



# Function with pass statement
def myfunction():
    pass
print() 


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
print()



