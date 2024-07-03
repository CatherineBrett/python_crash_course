# Exercise 4-1:

# pizzas = ["margherita", "calabrese", "fiorentina"]
# for pizza in pizzas:
#     print(f"One of my favourite pizzas is the {pizza.title()}.")
# print("I am trying to eat fewer pizzas.\n")


# Exercise 4-2:

# animals = ["cat", "dog", "squirrel"]
# for animal in animals:
#     print(f"A {animal} has a tail.")
# print("All of the animals above have tails.\n")


# Exercise 4-3:

# for value in range(1, 21):
#     print(value)


# Exercise 4-4:

# numbers = list(range(1, 1000001))
# for number in numbers:
#     print(number)


# Exercise 4-5:

# numbers_again = list(range(1, 1000001))
# print(min(numbers_again))
# print(max(numbers_again))
# print(sum(numbers_again))


# # Exercise 4-6:

# odd_numbers = list(range(1, 21, 2))
# for odd_number in odd_numbers:
#     print(odd_number)


# Exercise 4-7:

# multiples_of_three = list(range(3, 31, 3))
# for multiple_of_three in multiples_of_three:
#     print(multiple_of_three)


# Exercise 4-8:

# first_ten_cubes = []
# for value in range(1, 11):
#     cube = value**3
#     first_ten_cubes.append(cube)
#     print(cube)

# cubes = []
# for value in range(1, 11):
#     cubes.append(value**3)
#     print(value**3)


# Exercise 4-9:

# cubes = [value**3 for value in range(1, 11)]
# print(cubes)


# Exercise 4-10:

# animals = ["cat", "dog", "squirrel", "whale", "dolphin", "mongoose"]
# print(f"The first three items in this list are: {animals[:3]}.")
# print(f"Three items from the middle of the list are: {animals[2:5]}.")
# print(f"The last three items in the list are: {animals[-3:]}.")


# Exercise 4-11:

# my_pizzas = ["margherita", "calabrese", "fiorentina"]
# friend_pizzas = my_pizzas[:]

# my_pizzas.append("romagnola")
# friend_pizzas.append("capricciosa")

# print("My favourite pizzas are:")
# for pizza in my_pizzas:
#     print(pizza.title())

# print("\nMy friend's favourite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza.title())


# Exercise 4-12:

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("crisps")
friend_foods.append("nuts")

print("My favourite foods are:")
for item in my_foods:
    print(item)

print("\nMy friend's favourite foods are:")
for item in friend_foods:
    print(item)
