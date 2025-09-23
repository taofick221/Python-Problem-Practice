# Sort List Alphanumerically
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort() 
print(thislist)

# Sort Descending
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort(reverse=True)
print(thislist)



# Customize Sort Function
def myfunc(n):
  return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)



# Perform a case-insensitive sort of the list

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)




# Reverse the order of the list items

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
