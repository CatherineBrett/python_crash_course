from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text(encoding="utf-8")
print(f"{contents}\n")

lines = contents.splitlines()
for line in lines:
    print(line)