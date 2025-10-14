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

