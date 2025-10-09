# Removing Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print("After removing an item using pop():", thisdict)


# Removing an item using the del keyword
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print("After removing an item using del:", thisdict)    



# Removing the last inserted item using popitem() method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()      
print("After removing the last item using popitem():", thisdict)


# Clearing all items using clear() method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}  
thisdict.clear()
print("After clearing all items using clear():", thisdict)  



