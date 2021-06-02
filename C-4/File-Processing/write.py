# Writing a new file

# Look up help(open)

# with open("fruits.txt", "w") as myfile:
#     myfile.write("Apple\nCucumber\nOrange\n")
#     myfile.write("Banana")
#     print(myfile.read())


with open("fruis.txt", "a+") as myfile:
    myfile.write("\nKiwi")
    myfile.seek(0)
    content = myfile.read()

print(content)
