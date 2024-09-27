from pathlib import Path
import json


def print_fave_num():
    """Retrieve user's favourite number and print it."""
    path = Path("fave_number.json")
    contents = path.read_text()
    fave_num = json.loads(contents)
    print(f"I know your favourite number! It's {fave_num}!")


print_fave_num()
