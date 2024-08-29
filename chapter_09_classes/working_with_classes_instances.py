# Exercise 9-4


# class Restaurant:
#     """A simple attempt to model a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialise name and cuisine_type attibutes."""
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Print a restaurant's name and cuisine type."""
#         print(f"{self.name.title()} serves {self.cuisine_type.title()} food.")

#     def open_restaurant(self):
#         """Print a message to say the restaurant is open."""
#         print(f"{self.name.title()} is open.")

#     def set_number_served(self, number_served):
#         """Set the no. of customers served to the given value."""
#         self.number_served = number_served

#     def increment_number_served(self, no_of_customers):
#         """Add the given number to the overall number served."""
#         self.number_served += no_of_customers


# restaurant = Restaurant("dishoom", "indian")
# print(f"This restaurant has served {restaurant.number_served} customers.")

# restaurant.number_served = 100
# print(f"This restaurant has now served {restaurant.number_served} customers.")

# restaurant.set_number_served(200)
# print(f"This restaurant has now served {restaurant.number_served} customers.")

# restaurant.increment_number_served(300)
# print(f"The number of customers now served is {restaurant.number_served}.")


# Exercise 9-5


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, username, email, age):
        """Initialise a user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment no. of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        "Reset the no. of login attempts to 0."
        self.login_attempts = 0


joeb = User("joe", "bloggs", "joeb", "jbloggs@email.com", 29)

joeb.increment_login_attempts()
joeb.increment_login_attempts()
joeb.increment_login_attempts()
joeb.increment_login_attempts()
joeb.increment_login_attempts()

print(f"There have been {joeb.login_attempts} login attempts.")

joeb.reset_login_attempts()
print(f"login_attempts has now been reset to {joeb.login_attempts}.")
