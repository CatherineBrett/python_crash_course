# Exercise 7-8

sandwich_orders = ["tuna mayo", "cheese and tomato", "egg salad"]
finished_sandwiches = []

while sandwich_orders:
    filling = sandwich_orders.pop()

    print(f"I've made your {filling} sandwich.")
    finished_sandwiches.append(filling)

print("\nThe following sandwiches are ready:")
for filling in finished_sandwiches:
    print(filling)
