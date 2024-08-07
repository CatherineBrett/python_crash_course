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

sandwich_orders = [
    "pastrami",
    "tuna mayo",
    "pastrami",
    "cheese and tomato",
    "pastrami",
    "egg salad",
]
finished_sandwiches = []

print("We are currently out of pastrami - apologies for any inconvenience.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    filling = sandwich_orders.pop()
    finished_sandwiches.append(filling)

print("\nThe sandwiches we have been able to make are:")
for filling in finished_sandwiches:
    print(filling)
