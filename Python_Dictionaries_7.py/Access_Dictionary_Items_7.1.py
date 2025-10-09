# Get the value of the "model" key
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict["model"])



# The keys() method
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict.keys())


# The values() method
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict.values())


# The items() method
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict.items())



# Check if "model" is present in the dictionary
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
if "model" in thisdict:
    print("Key 'model' is present in the dictionary")
else:
    print("Key 'model' is not present in the dictionary")


