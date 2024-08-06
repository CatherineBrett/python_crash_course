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

# prompt = "\nEnter one pizza topping.(Or type 'quit' to finish): "

# response = ""

# while response != "quit":
#     response = input(prompt)

#     if response != "quit":
#         print(f"Thank you. We have added {response} to your pizza.")


# Exercise 7-5

# prompt = "\nHow old is the moviegoer? (Type 'quit' to exit): "

# response = ""

# while response != "quit":
#     response = input(prompt)

#     if response != "quit":
#         if int(response) < 3:
#             print("Tickets for children under 3yo are free!")
#         elif int(response) <= 12:
#             print("Tickets for children aged between 3 and 12 are $10 each.")
#         else:
#             print("Tickets for adults and children over 12 are $15.")


# Exercise 7-6
# variation on Exercise 7-4, using a break statement to exit the loop:

prompt = "\nEnter one pizza topping at a time. Type 'quit' to exit: "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"Thank you. We have added {topping} to your pizza.")
