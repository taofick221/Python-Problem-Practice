# Change tuple values
my_tuple = ("apple", "banana", "cherry")
mylist=list(my_tuple)
mylist[1] = "blueberry"
my_tuple=tuple(mylist)
print(my_tuple)

# Add items to a tuple
my_tuple = ("apple", "banana", "cherry")
mylist=list(my_tuple)
mylist.append("orange")
my_tuple=tuple(mylist)
print(my_tuple)



# Remove items from a tuple
my_tuple = ("apple", "banana", "cherry")
mylist = list(my_tuple)
mylist.remove("banana")
my_tuple = tuple(mylist)
print(my_tuple)

# Delete the tuple completely
my_tuple = ("apple", "banana", "cherry")    
del my_tuple
#print(my_tuple)  # This will raise an error because the tuple has been deleted 
# Output: NameError: name 'my_tuple' is not defined
# Uncommenting the above line will raise an error
# Note: Tuples are immutable, so we convert them to a list to make changes and then convert back to a tuple.

