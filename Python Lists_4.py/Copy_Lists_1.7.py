# Make a copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods.copy()
print(friend_foods)




# Another way to make a copy is to use the built-in list() function.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = list(my_foods)     
print(friend_foods)



# Make a copy of a list with the : operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
