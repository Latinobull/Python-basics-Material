# While Loops

# not practical

# a = 3

# while a > 0:
#     print(1)

# while True:
#     print(2)

# More practical
# username = ""

# while username != "python":
#     username = input("Enter username: ")


# Most Practical

while True:
    user = input("Enter username: ")
    if user == "python":
        print("this is the correct username")
        break
    else:
        print("Wrong username try again")
        continue
