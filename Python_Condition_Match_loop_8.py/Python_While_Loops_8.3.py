# With the while loop
i = 1
while i < 6:
    print(i)
    i += 1  
print() 

# With the break statement
i = 1
while True:
    if i == 6:
        break
    print(i)
    i += 1
print()


# With the continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print()


# With the else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Loop ended")

print()


# Nested while loop
i = 1
while i < 4:
    print("Outer loop:", i)
    j = 1
    while j < 3:
        print("  Inner loop:", j)
        j += 1
    i += 1
print()


