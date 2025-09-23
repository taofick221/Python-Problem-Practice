# Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print("After removing an item:", thisset)


# Removing an item that does not exist will raise an error
thisset = {"apple", "banana", "cherry"}
try:
    thisset.remove("orange")
except KeyError:
    print("Item not found")


# Using discard() method to remove an item
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print("After removing an item with discard():", thisset)

# Discarding an item that does not exist will not raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("orange")
print("After trying to remove a non-existent item with discard():", thisset)

# Using pop() method to remove a random item
thisset = {"apple", "banana", "cherry"}
removed_item = thisset.pop()
print("After removing a random item:", thisset)
print("Removed item:", removed_item)    

# Using clear() method to empty the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("After using clear():", thisset)

# Deleting the set entirely
thisset = {"apple", "banana", "cherry"}
del thisset 


