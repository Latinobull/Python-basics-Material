# # Limited arguments


# def newFunction(a, b, c):
#     return a * b * c


# print(newFunction(6, 3))

# Unlimited arguments
# use args for convention arbitrary


# def unlimited(*args):
#     return args


# print(unlimited(3, 4, 5, "2345", 342342.5, "hey", 1))


def unlimited(*args):
    product = 1
    for number in args:
        product = product * number
    return product


print(unlimited(2, 3, 20, 5, 7, 25, 10, "string"))

# Keyword arguments


def keyUnlimited(**kwargs):
    return kwargs


print(keyUnlimited(Mary=2, John=25, Bill=12, Dareen=30, Edwin=12.5))


# import pandas


# names = pandas.read_csv("people.csv")
# all_names = list(names["Name"])


# def student_Classrooom(*args):
#     for allname in args:
#         print("You have {} students in your class".format(len(allname)))
#         for fullname in allname:

#             print("Welcome " + str(fullname) + " to the Class")


# student_Classrooom(all_names)
