# Exercise 7-1

# car = input("Which type of rental car would you like? ")
# print(f"Please wait while we check if we have a {car} available.")


# Exercise 7-2

group_size = input("How many people are in your party? ")
group_size = int(group_size)

if group_size > 8:
    print("We will let you know as soon as a table is available.")
else:
    print("Thank you. Your table is ready.")
