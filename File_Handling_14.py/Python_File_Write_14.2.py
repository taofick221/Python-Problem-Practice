# Write to an Existing File
with open("demofile.txt","a") as f:
    f.write("\nNew text added")

with open("demofile.txt") as f:
    print(f.read())
    f.close()


# Overwrite Existing Content

with open("demofile.txt","w") as f:
    f.write("all text is deleted.New text added")

with open("demofile.txt") as f:
    print(f.read())
    f.close()