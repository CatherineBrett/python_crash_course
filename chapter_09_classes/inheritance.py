# Exercise 9-6


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


# class IceCreamStand(Restaurant):
#     """Represent aspects of a restaurant, specific to an ice cream stand."""

#     def __init__(self, name, cuisine_type):
#         """
#         Initialise attributes of the parent class.
#         Then initialise attributes specific to an ice cream stand.
#         """
#         super().__init__(name, cuisine_type)
#         self.flavours = ["vanilla", "chocolate", "strawberry"]

#     def display_flavours(self):
#         """Print a statement listing the ice cream stand's flavours."""
#         print(
#             f"The {self.name.title()} ice cream stand sells the following "
#             "flavours:"
#         )
#         for flavour in self.flavours:
#             print(f"\t{flavour}")


# my_stand = IceCreamStand("nice ices", "frozen")

# my_stand.display_flavours()


# Exercise 9-7


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


# class Admin(User):
#     """Represent aspects of a User, specific to an administrator."""

#     def __init__(self, first_name, last_name, username, email, age):
#         """
#         Initialise attributes of the parent class.
#         Then initialise attributes specific to an administrator.
#         """
#         super().__init__(first_name, last_name, username, email, age)
#         self.privileges = ["delete other users' posts", "delete users"]

#     def show_privileges(self):
#         """Print a statement listing an admin user's privileges."""
#         print("Admin users can also:")
#         for privilege in self.privileges:
#             print(f"\t- {privilege}")


# catherine = Admin("catherine", "brett", "admin1", "admin1@email.com", 41)

# catherine.show_privileges()


# Exercise 9-8


class Privileges:
    """A simple attempt to model privileges for an administrator."""

    def __init__(self):
        """Initialise privileges' attributes."""
        self.privileges = ["delete other users' posts", "delete users"]

    def show_privileges(self):
        """Print a statement listing an admin user's privileges."""
        print("Admin users can also:")
        for privilege in self.privileges:
            (print(f"\t- {privilege}"))


class Admin(User):
    """Represent aspects of a User, specific to an administrator."""

    def __init__(self, first_name, last_name, username, email, age):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, username, email, age)
        self.privileges = Privileges()


catherine = Admin("catherine", "brett", "cbrett", "cbrett@email.com", 41)

catherine.privileges.show_privileges()
