# Exercise 8-12


# def make_sandwich(*fillings):
#     """Print a summary of the sandwich the customer has ordered."""
#     print("\nYour sandwich has the following fillings:")
#     for filling in fillings:
#         print(f"\t- {filling}")


# make_sandwich("bacon", "lettuce", "tomato")
# make_sandwich("tuna", "sweetcorn")
# make_sandwich("cheese")


# Exercise 8-13


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "catherine",
#     "brett",
#     middle_name="jane",
#     location="birmingham",
#     field="software engineering",
# )

# print(user_profile)


# Exercise 8-14


def build_car_profile(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = build_car_profile("honda", "civic", colour="grey", doors=5)

print(car)
