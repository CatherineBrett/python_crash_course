# Exercise 7-4

# prompt = "\nEnter a pizza topping."
# prompt += "\n(Type 'quit' to finish): "

# active = True

# while active:
#     message = input(prompt)

#     if message == "quit":
#         active = False
#     else:
#         print(f"Thank you. We have added {message} to your pizza.")


# Exercise 7-4 version 2

prompt = "\nEnter one pizza topping.(Or type 'quit' to finish): "

response = ""

while response != "quit":
    response = input(prompt)

    if response != "quit":
        print(f"Thank you. We have added {response} to your pizza.")
