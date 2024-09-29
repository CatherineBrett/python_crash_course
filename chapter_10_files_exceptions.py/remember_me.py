from pathlib import Path
import json


def store_user_info(path):
    """Store a user's name, current hometown and favourite colour."""
    user_info = {}
    user_info["name"] = input("What is your name? ")
    user_info["hometown"] = input("What is your current hometown? ")
    user_info["fave_colour"] = input("What is your favourite colour? ")
    contents = json.dumps(user_info)
    path.write_text(contents)


def summarise_user_info(path):
    """Summarise the information stored about a user."""
    contents = path.read_text()
    info = json.loads(contents)
    print(
        f"Hi there, {info["name"]}! I remembered that your current hometown is "
        f"{info["hometown"]}, and that your favourite colour is "
        f"{info["fave_colour"]}!"
    )


stored_user_info = Path("stored_user_info.json")
store_user_info(stored_user_info)
summarise_user_info(stored_user_info)
