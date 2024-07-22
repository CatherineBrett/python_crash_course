#  Exercise 5-1, Conditional Tests

# dinner = "pizza"
# print("Is dinner == 'pizza'? I predict True.")
# print(dinner == "pizza")

# print("\nIs dinner == 'salad'? I predict False.")
# print(dinner == "salad")

# print(
#     "\nIs dinner == 'Pizza', given that testing for equality is case sensitive in Python? I predict False."
# )
# print(dinner == "Pizza")

# dessert = "bread and butter pudding"
# print("\nIs dessert == 'bread and butter pudding'? I predict True.")
# print(dessert == "bread and butter pudding")

# print("\nIs dessert == 'ice cream'? I predict False.")
# print(dessert == "ice cream")

# tv = "Million Dollar Listing"
# print("\nIs tv == 'Million Dollar Listing'? I predict True.")
# print(tv == "Million Dollar Listing")

# magazine = "Grazia"
# print("\nIs magazine == 'Grazia'? I predict True.")
# print(magazine == "Grazia")

# print("\nIs magazine == 'grazia'? I predict False.")
# print(magazine == "grazia")

# neighbourhood = "Harborne"
# print("\nIs neighbourhood != 'Harborne'? I predict False.")
# print(neighbourhood != "Harborne")

# number = 1000
# print("\nIs number < 2000? I predict True.")
# print(number < 2000)

# Exercise 5-2, More Conditional Tests

coding = "fun"
print("\nIs coding == 'fun'? I predict True.")
print(coding == "fun")

print("\nIs coding == 'no fun'? I predict False")
print(coding == "no fun")

print("\nIs coding != 'no fun'? I predict True.")
print(coding != "no fun")

print("\nIs coding != 'fun'? I predict False.")
print(coding != "fun")

author = "Iris Murdoch"
print("\nIs author.lower() == 'iris murdoch'? I predict True.")
print(author.lower() == "iris murdoch")

print("\nIs author.lower() == 'Iris Murdoch'? I predict False.")
print(author.lower() == "Iris Murdoch")

effort = 100
print("\nIs effort == 100? I predict True.")
print(effort == 100)

print("\nIs effort == 80? I predict False.")
print(effort == 80)

print("\nIs effort != 50? I predict True.")
print(effort != 50)

print("\nIs effort != 100? I predict False.")
print(effort != 100)

print("\nIs effort > 99? I predict True.")
print(effort > 99)

print(
    "\nIs effort > 100? I predict False because you can't give more than 100 per cent!"
)
print(effort > 100)

print("\nIs effort < 101? I predict True (see above!)")
print(effort < 101)

print("\nIs effort less than 100? I predict False.")
print(effort < 100)

print("\nIs effort >= 90? I predict True.")
print(effort >= 90)

print("\nIs effort >= 200? I predict False.")
print(effort >= 200)

print("\nIs effort <= 150? I predict True.")
print(effort <= 150)

print("\nIs effort <= 99? I predict False.")
print(effort <= 99)

num_1 = 5
num_2 = 4
print("\nAre num_1 and num_2 both greater than 3? I predict True.")
print(num_1 > 3 and num_2 > 3)

print("\nAre num_1 and num_2 both less than 5? I predict False.")
print(num_1 < 5 and num_2 < 5)

print("\nIs either num_1 or num_2 equal to 4? I predict True.")
print(num_1 == 4 or num_2 == 4)

print("\nIs either of the nums (num_1 or num_2) equal to 10? I predict False.")
print(num_1 == 10 or num_2 == 10)

some_neighbours_characters = ["susan kennedy", "karl kennedy", "toadfish rebecchi"]
print(
    "\nDoes the list some_neighbours_characters contain 'toadfish rebecchi'? I predict True."
)
print("toadfish rebecchi" in some_neighbours_characters)

print("\nDoes the list contain 'gail platt'? I predict False.")
print("gail platt" in some_neighbours_characters)

print("\nDoes the list NOT contain 'audrey roberts'? I predict True.")
print("audrey roberts" not in some_neighbours_characters)

print(
    "\nDoes the list some_neighbours_characters NOT contain 'susan kennedy'? I predict False."
)
print("susan kennedy" not in some_neighbours_characters)
