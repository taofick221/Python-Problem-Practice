# Loop through a tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Loop through the index numbers
fruits = ("apple", "banana", "cherry")     
for i in range(len(fruits)):
    print(fruits[i])
    print(i)
    print(fruits[i])


# Looping with while
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1  
# Note: Tuples are immutable, so we cannot change their values directly. We can only loop through them.
# Output:
# apple 
# banana
# cherry
# The loop goes through each item in the tuple and prints it.


