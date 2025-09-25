# If condition
a = 33
b = 200
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")


# Elif condition
a = 33
b = 200
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")


# Short hand if...else
a = 200
b = 33  
print("a is greater than b") if a > b else print("a is not greater than b") 



# Nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


