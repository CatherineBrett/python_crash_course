# Exercise 9-6


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialise name and cuisine_type attibutes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a restaurant's name and cuisine type."""
        print(f"{self.name.title()} serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Print a message to say the restaurant is open."""
        print(f"{self.name.title()} is open.")

    def set_number_served(self, number_served):
        """Set the no. of customers served to the given value."""
        self.number_served = number_served

    def increment_number_served(self, no_of_customers):
        """Add the given number to the overall number served."""
        self.number_served += no_of_customers


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to an ice cream stand."""

    def __init__(self, name, cuisine_type):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an ice cream stand.
        """
        super().__init__(name, cuisine_type)
        self.flavours = ["vanilla", "chocolate", "strawberry"]

    def display_flavours(self):
        """Print a statement listing the ice cream stand's flavours."""
        print(
            f"The {self.name.title()} ice cream stand sells the following "
            "flavours:"
        )
        for flavour in self.flavours:
            print(f"\t{flavour}")


my_stand = IceCreamStand("nice ices", "frozen")

my_stand.display_flavours()
