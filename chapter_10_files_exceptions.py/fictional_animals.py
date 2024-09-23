from pathlib import Path


def print_names(path):
    """Print the fictional animals named in a given file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} cannot be found.")
    else:
        # Not bothering with splitlines() here as only printing to screen
        # as opposed to wanting to access/modify elements in a list
        print(f"{contents}\n")


filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    file = Path(filename)
    print_names(file)
