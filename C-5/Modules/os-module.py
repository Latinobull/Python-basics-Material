import time

import os


while True:
    if os.path.exists("fruits.txt"):

        with open("fruits.txt") as file:
            print(file.read())

    else:
        print("File does not exist, lets make it for you")
        open("fruits.txt", "x")
    time.sleep(5)