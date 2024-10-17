from city_functions import get_formatted_place


def test_city_country():
    """Do placenames like 'Birmingham, England' work?"""
    formatted_place = get_formatted_place("birmingham", "england")
    assert formatted_place == "Birmingham, England"


def test_city_country_population():
    """Does place info like 'Birmingham, England - population 1144900' work?"""
    formatted_place = get_formatted_place(
        "birmingham", "england", population=1144900
    )
    assert formatted_place == "Birmingham, England - population 1144900"
