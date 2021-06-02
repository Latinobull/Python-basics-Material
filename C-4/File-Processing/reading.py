# myfile = open("names.txt")
# print(myfile.read())
# myfile.seek(0)
# print(myfile.read())
# myfile.close()

# cursor concept


# with context manager
with open("names.txt") as myfile:
    content = myfile.read()

print(content)
print(content)

# look into help(open)
