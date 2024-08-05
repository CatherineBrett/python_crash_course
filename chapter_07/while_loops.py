# Exercise 7-4

prompt = "\nEnter a pizza topping."
prompt += "\n(Type 'quit' to finish): "

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(f"Thank you. We have added {message} to your pizza.")
