def class_grade(grade):
    if grade >= 65:
        return "You Passed with a %i" % grade
    else:
        return "You Failed with a %i" % grade


grade_input = int(input("Enter your grade:"))

print(class_grade(grade_input))


# name = input("Enter your name: ")

# print(name)
