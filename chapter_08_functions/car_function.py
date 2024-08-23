def build_car_profile(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    print(car_info)
