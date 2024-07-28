# Exercise 6-7

# an_on = {"first_name": "an", "last_name": "on", "age": 1000, "city": "naples"}
# jbloggs = {"first_name": "joe", "last_name": "bloggs", "age": 50, "city": "bonn"}
# cnewport = {
#     "first_name": "cal",
#     "last_name": "newport",
#     "age": 42,
#     "city": "washington, d.c.",
#     }

# people = [an_on, jbloggs, cnewport]

# for person in people:
#     print(person)


# Exercise 6-8

# bobby = {"animal": "dog", "owner": "sue"}
# india = {"animal": "dog", "owner": "maala"}
# chase = {"animal": "cat", "owner": "jules"}
# freddy = {"animal": "fox", "owner": "colette"}

# pets = [bobby, india, chase, freddy]

# for pet in pets:
#     print(pet)


# Exercise 6-9

# favorite_places = {
#     "jim": ["paris", "lille"],
#     "frank": ["berlin"],
#     "deirdre": ["seville", "lisbon", "madeira"],
# }

# for name, places in favorite_places.items():
#     if len(places) < 2:
#         print(f"\n{name.title()}'s favorite place is:")
#     else:
#         print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")


# Exercise 6-10

fave_numbers = {
    "john": [1, 6],
    "paul": [3],
    "george": [9, 12, 20],
    "ringo": [0, 300],
    "pete": [7],
}

for name, numbers in fave_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
