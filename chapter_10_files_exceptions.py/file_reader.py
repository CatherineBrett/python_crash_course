from pathlib import Path


path = Path("pi_digits.txt")
contents = path.read_text().rstrip()
print(contents)
print("Blank line still not there.")
