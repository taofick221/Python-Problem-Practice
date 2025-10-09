# Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print("After adding an item:", thisset)


# Adding multiple items to a set using update() method
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "grape"])
print("After adding multiple items:", thisset)


# Adding items from another set
thisset1 = {"apple", "banana", "cherry"}
thisset2 = {"orange", "grape"}
thisset1.update(thisset2)
print("After adding items from another set:", thisset1)

# Adding items from a list
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "grape"])
print("After adding items from a list:", thisset)   


# Adding items from a tuple
thisset = {"apple", "banana", "cherry"}
thisset.update(("orange", "grape"))
print("After adding items from a tuple:", thisset)  

