# Remove the file
import os
os.remove("demofil.txt")



# Check if File exist
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")

else:
    print("the file does not exists")