result = []

# while true loop
# user input
# Key words that format the string whether use question mark or period


def sentence_maker(phrase):
    question_words = ("Who", "What", "When", "Where", "Why", "How")
    capitalized = phrase.capitalize()
    if phrase.startswith(question_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


while True:
    user_input = input("Say Something: ")

    if user_input == "/end":
        newSentence = " ".join(result)
        break
    else:
        result.append(sentence_maker(user_input))

print(newSentence)
