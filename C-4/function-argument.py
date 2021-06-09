# # Limited arguments


# def newFunction(a, b,):
#     return a * b


# print(newFunction(6, 3, 2))

# Unlimited arguments
# use args for convention arbitrary


# def unlimited(*args):
#     return args


# print(unlimited(3, 4, 5, "2345", 342342.5, "hey", 1, 3, 2495254, 12.12))


# def unlimited(*args):
#     result = 0
#     for number in args:
#         result = result + number
#     return result


# print(unlimited(2, 3, 12, 24, 2))

# Keyword arguments


# def keyUnlimited(**kwargs):
#     return kwargs


# print(keyUnlimited(Mary=2, John=25, Bill=12, Dareen=30, Edwin=12.5, Samya=10))


import pandas


names = pandas.read_csv("people.csv")
all_names = str(names["Name"])

print(all_names)

# def student_Classrooom(*args):
#     # for allname in args:
#     #     print("You have {} students in your class".format(len(allname)))
#     #     for fullname in allname:

#     #         print("Welcome " + str(fullname) + " to the Class")


# student_Classrooom(all_names)
