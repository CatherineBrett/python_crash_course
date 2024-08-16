# Exercise 8-12


def make_sandwich(*fillings):
    """Print a summary of the sandwich the customer has ordered."""
    print("\nYour sandwich has the following fillings:")
    for filling in fillings:
        print(f"\t- {filling}")


make_sandwich("bacon", "lettuce", "tomato")
make_sandwich("tuna", "sweetcorn")
make_sandwich("cheese")
