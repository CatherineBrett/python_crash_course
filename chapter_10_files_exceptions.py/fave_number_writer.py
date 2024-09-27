from pathlib import Path
import json


def store_fave_num():
    """Prompt user for their favourite number and store it."""
    fave_num = input("What is your favourite number? ")
    path = Path("fave_number.json")
    contents = json.dumps(fave_num)
    path.write_text(contents)


store_fave_num()
