from random import randint, choice


# class Die:
#     """A simple attempt to model a die."""

#     def __init__(self, sides=6):
#         """Initialise attributes to describe a die."""
#         self.sides = sides

#     def roll_die(self):
#         """Print a random number between 1 and the no. of sides the die has
#         (inclusive).
#         """
#         rand_no = randint(1, self.sides)
#         print(rand_no)


# six_sided_die = Die()
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

# ten_sided_die = Die(10)
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

# twenty_sided_die = Die(20)
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

# lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

# winning_nums_letters = []

# while len(winning_nums_letters) < 4:
#     drawn_num_letter = choice(lottery)
#     if drawn_num_letter not in winning_nums_letters:
#         winning_nums_letters.append(drawn_num_letter)

# print("Tickets matching these four numbers or letters win a prize:")
# for drawn_num_letter in winning_nums_letters:
#     print(drawn_num_letter)


# Exercise 9-15
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers
# until your ticket wins. Print a msg reporting how many times the loop had to
# run to give you a winning ticket.


def get_winning_nums(poss_nums):
    """Draw the four winning numbers from the list of possible numbers."""
    winning_nums = []
    while len(winning_nums) < 4:
        drawn_num = choice(poss_nums)
        if drawn_num not in winning_nums:
            winning_nums.append(drawn_num)
    return winning_nums


def check_ticket(ticket, winning_nums):
    """Check if a ticket has all the winning numbers."""
    for num in ticket:
        if num not in winning_nums:
            return False
    return True


lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
my_ticket = [2, 5, 9, 14]
attempts = 0
winner = False
maximum_attempts = 1_000_000

while not winner:
    winning_ticket = get_winning_nums(lottery)
    winner = check_ticket(my_ticket, winning_ticket)
    attempts += 1
    if attempts >= maximum_attempts:
        break

if winner:
    print(
        f"You have won the lottery! Your numbers were {my_ticket} and the "
        f"drawn numbers were {winning_ticket}. It took {attempts} attempts."
    )
else:
    print(f"Sorry! We tried {maximum_attempts} times and you didn't win :(")
