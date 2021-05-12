# Python for loops are soooooooooooo easy


# Basic
integ = [3.4, 4.2, 5.6]
for newInteg in integ:
    print(round(newInteg))

    print("Done")

# Loop through a string
for new in "hello":
    print(new)
    print("--------")

# # Loop through dictionary
student_grades = {"Marry": 10.2, "Sim": 6.8, "John": 8.3}
# items, keys, values
for grades in student_grades.items():
    print(grades[1])

# # What is the problem with these new for loops?
# # Python2
temps = [67.3, 82.2, 71.9]
newTemp = []

for temp in temps:
    newTemp.append(temp)

print(newTemp)

# list comprehension
temps2 = [67.3, 82.2, 71.9]
newArray = [yellow for yellow in temps2]

print(newArray)