# open() function.
f= open("demofile.txt")
print(f.read())



# Using the with statement

with open("demofile.txt") as file:
    print(file.read())
    file.close()

# Read Lines

with open("demofile.txt") as file:
    print(file.readline())
    file.close()


