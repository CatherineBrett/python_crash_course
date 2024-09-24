from pathlib import Path


def count_the(path):
    """Count the number of times the word 'the' appears in a given text."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, {path} was not found.")
    else:
        instances_of_the = contents.lower().count("the ")
        print(
            f"The word 'the' appears in the file {path} {instances_of_the} times."
        )


filenames = ["bleak_house.txt", "therese_raquin.txt", "diary_nobody.txt"]
for filename in filenames:
    file = Path(filename)
    count_the(file)
