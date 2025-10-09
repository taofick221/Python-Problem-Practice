# Loop through a dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict:
    print(key, thisdict[key])   
print()

# Loop through the keys
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict.keys():
    print(key)  
print()


# Loop through the values
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for value in thisdict.values():
    print(value)    
print()


# Loop through both keys and values, using the items() method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key, value in thisdict.items():
    print(key, value)   
print()

