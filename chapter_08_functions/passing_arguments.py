# Exercise 8-3


def make_shirt(size, text):
    """Display info about a shirt's size and its printed text."""
    print(
        f"\nThe shirt is size {size} and has the following text printed on it: "
        f"{text}."
    )


make_shirt("small", "This is my favourite t-shirt")
make_shirt(text="This is my second-favourite t-shirt", size="medium")
