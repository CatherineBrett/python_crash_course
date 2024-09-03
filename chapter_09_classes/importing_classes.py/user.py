"""A set of classes that can be used to represent users."""


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


class Privileges:
    """A simple attempt to model privileges for an administrator."""

    def __init__(self):
        """Initialise privileges' attributes."""
        self.privileges = ["delete other users' posts", "delete users"]

    def show_privileges(self):
        """Print a statement listing an admin user's privileges."""
        print("As an administrator, this user is permitted to:")
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
