# Exercise 9-1


# class Restaurant:
#     """A simple attempt to model a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialise name and cuisine_type attibutes."""
#         self.name = name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Print a restaurant's name and cuisine type."""
#         print(f"{self.name.title()} serves {self.cuisine_type.title()} food.")

#     def open_restaurant(self):
#         """Print a message to say the restaurant is open."""
#         print(f"{self.name.title()} is open.")


# restaurant = Restaurant("la plancha", "spanish")

# print(restaurant.name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# Exercise 9-2

# restaurant_one = Restaurant("dishoom", "indian")
# restaurant_two = Restaurant("gaucho", "argentinian")
# restaurant_three = Restaurant("sabai sabai", "thai")

# restaurant_one.describe_restaurant()
# restaurant_two.describe_restaurant()
# restaurant_three.describe_restaurant()


# Exercise 9-3


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, username, email, age):
        """Initialise a user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age

    def describe_user(self):
        """Print a summary of the user's information."""
        print(
            f"The user with username '{self.username}' is called "
            f"{self.first_name.title()} {self.last_name.title()} and they are"
            f" {self.age} years old. Their email address is {self.email}."
        )

    def greet_user(self):
        """Print a personalised greeting to the user."""
        print(f"Hello there, {self.username}!")


catherine = User("catherine", "brett", "cbrett", "cbrett@email.com", 41)
acurtain = User("annette", "curtain", "acurtain", "acurtain@email.com", 65)
joeb = User("joe", "bloggs", "joeb", "jbloggs@email.com", 29)

catherine.describe_user()
catherine.greet_user()
acurtain.describe_user()
acurtain.greet_user()
joeb.describe_user()
joeb.greet_user()
