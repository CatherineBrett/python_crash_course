# Exercise 10-6

# def add_nums():
#     """Prompt user for two numbers and print the sum."""
#     first_num = input("Enter a number (in digits): ")
#     second_num = input("Enter another number (also in digits): ")
#     try:
#         added = int(first_num) + int(second_num)
#     except ValueError:
#         print("Please provide digits rather than text.")
#     else:
#         print(f"The sum of your two numbers is {added}.")


# add_nums()


# Exercise 10-7


def add_nums():
    """Prompt user for two numbers and print the sum."""
    while True:
        first_prompt = "\nEnter a number (in digits)."
        first_prompt += "\nAlternatively, you can enter 'quit' to exit: "
        second_prompt = "\nEnter another number (also in digits)."
        second_prompt += "\nAgain, you can enter 'quit' to exit: "
        first_num = input(first_prompt)
        if first_num == "quit":
            break
        second_num = input(second_prompt)
        if second_num == "quit":
            break
        try:
            added = int(first_num) + int(second_num)
        except ValueError:
            print("\nPlease provide digits rather than text.")
        else:
            print(f"\nThe sum of your two numbers is {added}.")


add_nums()
