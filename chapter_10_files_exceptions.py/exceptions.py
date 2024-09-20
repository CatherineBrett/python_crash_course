def add_nums():
    """Prompt user for two numbers and print the sum."""
    first_num = input("Enter a number (in digits): ")
    second_num = input("Enter another number (also in digits): ")
    try:
        added = int(first_num) + int(second_num)
    except ValueError:
        print("Please provide digits rather than text.")
    else:
        print(f"The sum of your two numbers is {added}.")


add_nums()
