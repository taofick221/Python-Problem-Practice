# Packing a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)


# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a)
print(b)
print(c)

# Unpacking with asterisk
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
a, b, *c = fruits
print(a)
print(b)
print(c)    
# a will be "apple", b will be "banana", c will be a list containing the rest of the items
