from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


# is there a user in storage?
# if no, prompt for a new username
# if yes, is that user the same as the current user?
# if yes, welcome them back
# if no, prompt for a new username
def greet_user(path):
    """Greet the user by name."""
    previous_user = get_stored_username(path)
    if not previous_user:
        username = get_new_username(path)
        print(f"We'll remember you next time, {username}!")
    else:
        current_user = input(f"Hello! Is this {previous_user}? Enter y/n: ")
        if current_user == "y":
            print(f"Welcome back, {previous_user}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you next time, {username}!")


stored_user = Path("stored_user.json")
greet_user(stored_user)
