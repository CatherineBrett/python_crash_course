# Exercise 7-1

# car = input("Which type of rental car would you like? ")
# print(f"Please wait while we check if we have a {car} available.")


# Exercise 7-2

# group_size = input("How many people are in your party? ")
# group_size = int(group_size)

# if group_size > 8:
#     print("We will let you know as soon as a table is available.")
# else:
#     print("Thank you. Your table is ready.")


# Exercise 7-3

number = input("Choose a number and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is indeed a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")
