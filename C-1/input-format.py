user_input = input("Enter your name: ")
user_input2 = int(input("Enter your age:"))
# input_now = "charlie"
# message = "Hello %s! You are %i years old!" % (user_input, user_input2)

# print(message)

message2 = "Welcome to Python Class {} You are {} years old".format(
    user_input, user_input2
)
print(message2)
