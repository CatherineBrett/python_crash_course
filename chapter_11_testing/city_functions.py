# def get_formatted_place(city, country):
#     """Generate a neatly formatted placename."""
#     placename = f"{city}, {country}"
#     return placename.title()


def get_formatted_place(city, country, population=""):
    """Generate neatly formatted location info."""
    if population:
        place = f"{city.title()}, {country.title()} - population {population}"
    else:
        place = f"{city.title()}, {country.title()}"
    return place
