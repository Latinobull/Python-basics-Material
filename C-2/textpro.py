results = []


def sentence_maker(phrase):
    question_words = ("Who", "What", "When", "Where", "Why", "How")
    capitalized = phrase.capitalize()
    if phrase.startswith(question_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        newSentence = " ".join(results)
        break
    else:
        results.append(sentence_maker(user_input))

print(newSentence)
