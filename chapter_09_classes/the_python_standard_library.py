from random import randint, choice


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialise attributes to describe a die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the no. of sides the die has
        (inclusive).
        """
        rand_no = randint(1, self.sides)
        print(rand_no)


six_sided_die = Die()
# print("Rolling my six-sided die ten times:")
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()
# six_sided_die.roll_die()

ten_sided_die = Die(10)
# print("\nRolling my ten-sided die ten times:")
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()
# ten_sided_die.roll_die()

twenty_sided_die = Die(20)
# print("\nRolling my twenty-sided die ten times:")
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()
# twenty_sided_die.roll_die()


# Exercise 9-14

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winning_nums_letters = []

while len(winning_nums_letters) < 4:
    drawn_num_letter = choice(lottery)
    if drawn_num_letter not in winning_nums_letters:
        winning_nums_letters.append(drawn_num_letter)

print("Tickets matching these four numbers or letters win a prize:")
for drawn_num_letter in winning_nums_letters:
    print(drawn_num_letter)
