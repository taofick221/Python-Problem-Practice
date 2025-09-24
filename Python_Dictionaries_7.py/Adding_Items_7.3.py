# Adding Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"   
print("After adding an item:", thisdict)


# Adding an item using the update() method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})   
print("After adding an item using update():", thisdict)


# Adding items from another dictionary using update() method
thisdict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict2 = {"color": "red", "price": 30000}
thisdict1.update(thisdict2)   
print("After adding items from another dictionary:", thisdict1)


