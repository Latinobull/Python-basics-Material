# list comprehension
# Data science
temps2 = [67.3, 82.2, 71.9]
newTemp2 = [temp.__round__() for temp in temps2]

# print(newTemp2)

# with if statement
temps = [67.3, 82.2, -9999, 71.9, 60.4, -9999, 47.6]
newTemps = [temp / 2 for temp in temps if temp != -9999]

print(newTemps)

# with if else statement
temps3 = [67.3, 82.2, -9999, 71.9, 60.4, -9999, 47.6]
newTemps3 = [temp / 2 if temp != -9999 else 0 for temp in temps3]

print(newTemps3)

# # Where does the else goes?