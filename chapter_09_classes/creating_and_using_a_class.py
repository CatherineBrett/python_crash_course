# Exercise 9-1


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialise name and cuisine_type attibutes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a restaurant's name and cuisine type."""
        print(f"{self.name.title()} serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Print a message to say the restaurant is open."""
        print(f"{self.name.title()} is open.")


restaurant = Restaurant("la plancha", "spanish")

print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
