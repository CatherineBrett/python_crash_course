# Exercise 6-1

an_on = {"first_name": "an", "last_name": "on", "age": 1000, "city": "naples"}
print(f"This person's first name is {an_on["first_name"].title()}.")
print(f"Their last name is {an_on["last_name"].title()}.")
print(f"They are {an_on["age"]} years old.")
print(f"They live in {an_on["city"].title()}.\n")


# Exercise 6-2

fave_numbers = {
    "john": 1,
    "paul": 3,
    "george": 9,
    "ringo": 6,
    "pete": 7,
    }

print(fave_numbers)


# Exercise 6-3

glossary = {
    "variable": "a label you can assign to a value",
    "string": "anything inside quotes",
    "float": "any number with a decimal point",
    "list": "a collection of items in a particular order",
    "tuple": "an immutable list",
    }

term = glossary["variable"]
print(f"\nVariable: {term}\n")

term = glossary["string"]
print(f"String: {term}\n")

term = glossary["float"]
print(f"Float: {term}\n")

term = glossary["list"]
print(f"List: {term}\n")

term = glossary["tuple"]
print(f"Tuple: {term}\n")
