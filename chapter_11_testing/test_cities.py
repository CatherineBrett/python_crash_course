from city_functions import get_formatted_place


def test_city_country():
    """Do placenames like 'Birmingham, England' work?"""
    formatted_placename = get_formatted_place("birmingham", "england")
    assert formatted_placename == "Birmingham, England"
