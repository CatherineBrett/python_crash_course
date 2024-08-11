# Exercise 8-6


# def city_country(city, country):
#     """Return the name of a city and the country in which it is located,
#     neatly formatted."""
#     city_and_country = f"{city}, {country}"
#     return city_and_country.title()


# first_city = city_country("liverpool", "england")
# second_city = city_country("swansea", "wales")
# third_city = city_country("aberdeen", "scotland")
# print(first_city)
# print(second_city)
# print(third_city)


# Exercise 8-7


def make_album(artist, album, no_of_songs=None):
    """Return a dictionary containing information about an album."""
    album_info = {"artist": artist, "album": album}
    if no_of_songs:
        album_info["no. of songs"] = no_of_songs
    return album_info


first_album = make_album("super furry animals", "guerrilla")
second_album = make_album("patti smith", "horses")
third_album = make_album("the strokes", "room on fire")
fourth_album = make_album("supergrass", "i should coco", 13)

print(first_album)
print(second_album)
print(third_album)
print(fourth_album)
