import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def dictionary(word):
    return word


user_input = input("What word do you want to search: ")
print(dictionary(user_input))