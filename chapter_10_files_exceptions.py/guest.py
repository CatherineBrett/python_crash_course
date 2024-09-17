from pathlib import Path

# guest = input("What is your name? ")
# path = Path("guest.txt")
# path.write_text(guest)

prompt = "\nWhat is your name?"
prompt += "\n(Or enter 'quit' to exit): "

guest_list = ""

while True:
    guest = input(prompt)

    if guest == "quit":
        break
    else:
        guest_list += f"{guest}\n"

path = Path("guest_book.txt")
path.write_text(guest_list)
