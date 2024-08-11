# Exercise 8-6


def city_country(city, country):
    """Return the name of a city and the country in which it is located,
    neatly formatted."""
    city_and_country = f"{city}, {country}"
    return city_and_country.title()


first_city = city_country("liverpool", "england")
second_city = city_country("swansea", "wales")
third_city = city_country("aberdeen", "scotland")
print(first_city)
print(second_city)
print(third_city)
