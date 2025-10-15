# Exception Handling
try:
    print(x)
except NameError:
    print("Varible x is not defined")
except:
    print("Other error")



# Try to open and write to a file that is not writable
try:
    f=open("demofile.txt","w")

    try:
        f.write("Hi,how are you")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
        print("Successfull")

except:
    print("Something went wrong when opening the file")

# Raise an error and stop the program if x is lower than 0

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# Raise a TypeError if x is not an integer

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")




# list and a dictionary with try and except
try:
    fruits = ["apple", "banana", "cherry"]
    prices = {"apple": 100, "banana": 60, "cherry": 120}

    print(fruits[5])  

    print(prices["mango"])  

except IndexError:
    print("List index is out of range!")

except KeyError:
    print("Key not found in dictionary!")

finally:
    print("Program finished.")
