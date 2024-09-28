from pathlib import Path
import json


def get_stored_fave_num(path):
    """Return user's favourite number if one is stored."""
    if path.exists():
        contents = path.read_text()
        fave_num = json.loads(contents)
        return fave_num
    return None


def store_fave_num(path):
    """Prompt user for their favourite number and store it."""
    fave_num = input("What is your favourite number? ")
    contents = json.dumps(fave_num)
    path.write_text(contents)
    return fave_num


def display_fave_num(path):
    """Print user's favourite number if previously stored, or ask for one."""
    # In the examples in the book, they assign the return value of the functions
    # to a variable and use the variable in the f-string instead of using inline
    # funtion calls like I have here:
    if get_stored_fave_num(path):
        print(f"Your favourite number is {get_stored_fave_num(path)}!")
    else:
        print(
            f"We will remember that your favourite number is "
            f"{store_fave_num(path)}!"
        )


number_store = Path("favourite_number.json")
display_fave_num(number_store)
