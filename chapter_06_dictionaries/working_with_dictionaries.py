# Exercise 6-1

# an_on = {"first_name": "an", "last_name": "on", "age": 1000, "city": "naples"}
# print(f"This person's first name is {an_on["first_name"].title()}.")
# print(f"Their last name is {an_on["last_name"].title()}.")
# print(f"They are {an_on["age"]} years old.")
# print(f"They live in {an_on["city"].title()}.\n")


# Exercise 6-2

# fave_numbers = {
#     "john": 1,
#     "paul": 3,
#     "george": 9,
#     "ringo": 6,
#     "pete": 7,
#     }

# print(fave_numbers)


# Exercises 6-3 and 6-4

# glossary = {
#     "variable": "a label you can assign to a value",
#     "string": "anything inside quotes",
#     "whitespace": "any nonprinting characters, such as spaces, tabs, and newlines",
#     "float": "any number with a decimal point",
#     "index error": "occurs when Python can't find an item at the index you requested",
#     "list": "a collection of items in a particular order",
#     "tuple": "an immutable list",
#     "boolean expression": "another name for a conditional test",
#     "dictionary": "a collection of key-value pairs",
#     "key-value pair": "a set of values associated with each other",
#     }

# definition = glossary["variable"]
# print(f"\nVariable: {definition}\n")

# definition = glossary["string"]
# print(f"String: {definition}\n")

# definition = glossary["float"]
# print(f"Float: {definition}\n")

# definition = glossary["list"]
# print(f"List: {definition}\n")

# definition = glossary["tuple"]
# print(f"Tuple: {definition}\n")

# for term, definition in glossary.items():
#     print(f"\n{term.title()}: {definition}")


# Exercise 6-5

# river_locations = {
#     "yellow river": "china",
#     "mississippi": "north america",
#     "yangtze": "china",
# }

# for river, location in river_locations.items():
#     print(f"\nThe {river.title()} flows through {location.title()}.")

# print("\nHere is a list of every river in my river_locations dictionary:")
# for river in river_locations.keys():
#     print(river.title())

# print(
#     "\nHere is a list of every location in my river_locations dictionary, with repetitions included:"
# )
# for location in river_locations.values():
#     print(location.title())


# Exercise 6-6

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

peeps_to_poll = ["catherine", "jen", "mike", "sarah", "martin"]

for name in peeps_to_poll:
    if name in favourite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"Hi, {name.title()}! Please take a moment to complete the poll.")
