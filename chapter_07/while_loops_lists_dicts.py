# Exercise 7-8

# sandwich_orders = ["tuna mayo", "cheese and tomato", "egg salad"]
# finished_sandwiches = []

# while sandwich_orders:
#     filling = sandwich_orders.pop()

#     print(f"I've made your {filling} sandwich.")
#     finished_sandwiches.append(filling)

# print("\nThe following sandwiches are ready:")
# for filling in finished_sandwiches:
#     print(filling)


# Exercise 7-9

# sandwich_orders = [
#     "pastrami",
#     "tuna mayo",
#     "pastrami",
#     "cheese and tomato",
#     "pastrami",
#     "egg salad",
# ]
# finished_sandwiches = []

# print("We are currently out of pastrami - apologies for any inconvenience.")

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     filling = sandwich_orders.pop()
#     finished_sandwiches.append(filling)

# print("\nThe sandwiches we have been able to make are:")
# for filling in finished_sandwiches:
#     print(filling)


# Exercise 7-10

responses = {}

polling_active = True

while polling_active:

    name = input("\nWhat is your name? ")
    response = input("\nWhat is your number one dream holiday destination? ")

    responses[name] = response

    repeat = input(
        "\nWould you like to allow another person to respond to the poll? (y/n): "
    )

    if repeat == "n":
        polling_active = False

print("\nThe results of the poll are:")
for name, response in responses.items():
    print(f"\t{name}'s dream holiday destination is {response}!")

print(f"\nThe responses dictionary looks like this: {responses}")
