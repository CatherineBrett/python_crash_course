"""A class that can be used to represent a user."""


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
