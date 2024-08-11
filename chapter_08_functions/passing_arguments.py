# Exercise 8-3


# def make_shirt(size, text):
#     """Display info about a shirt's size and its printed text."""
#     print(
#         f"\nThe shirt is size {size} and has the following text printed on it: "
#         f"{text}."
#     )


# make_shirt("small", "This is my favourite t-shirt")
# make_shirt(text="This is my second-favourite t-shirt", size="medium")


# Exercise 8-4


# def make_shirt(size="large", text="I love Python"):
#     """Display info about a shirt's size and its printed text."""
#     print(
#         f"\nThe shirt is size {size} and has the following text printed on it: "
#         f"{text}."
#     )


# make_shirt()
# make_shirt("medium")
# make_shirt("small", "I am learning Python")
# make_shirt(text="I love programming", size="medium")


# Exercise 8-5


def describe_city(city, country="england"):
    """Displays a sentence naming a city and the country in which it is
    located."""
    print(f"{city.title()} is in {country.title()}.")


describe_city("birmingham")
describe_city("cardiff", "wales")
describe_city(country="scotland", city="glasgow")
