"""
importing 
JS
import Card from '@materialui/core'

Python to open file 
open()
"""
"""
inputs
while 
if else statements
built in methods
"""
import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        did_you = input(
            "Did you mean {} instead? Y for yes, N for no: ".format(
                get_close_matches(word, data.keys())[0]
            )
        )
        if did_you == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word not found, please check your spelling"

    else:
        return "Not a word"


user_input = input("What word do you want to search: ")

"""
Question: How do we make the output of the code cleaner and more user friendly instead of a blob of definitions?
"""

print(dictionary(user_input))