# Exercise 9-4


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


restaurant = Restaurant("dishoom", "indian")
print(f"This restaurant has served {restaurant.number_served} customers.")

restaurant.number_served = 100
print(f"This restaurant has now served {restaurant.number_served} customers.")

restaurant.set_number_served(200)
print(f"This restaurant has now served {restaurant.number_served} customers.")

restaurant.increment_number_served(300)
print(f"The number of customers now served is {restaurant.number_served}.")
