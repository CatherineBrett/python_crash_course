"""A set of classes that can be used to represent admin users."""

from user import User


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
