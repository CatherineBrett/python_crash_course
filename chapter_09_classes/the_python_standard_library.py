from random import randint


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
print("Rolling my six-sided die ten times:")
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()

ten_sided_die = Die(10)
print("\nRolling my ten-sided die ten times:")
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
print("\nRolling my twenty-sided die ten times:")
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
