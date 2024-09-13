from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()
print(f"{contents}\n")

lines = contents.splitlines()
for line in lines:
    print(line)
