names = ["pippa", "jules", "laura"]

print(names[0])
print(names[1])
print(names[2])

message_1 = f"Congratulations, {names[0]}! You have made it on to my list!"
message_2 = f"Congratulations, {names[1]}! You have made it on to my list!"
message_3 = f"Congratulations, {names[2]}! You have made it on to my list!"

print(message_1)
print(message_2)
print(message_3)

# Capitalise the names:
message_1 = f"Congratulations, {names[0].title()}! You have made it on to my list!"
message_2 = f"Congratulations, {names[1].title()}! You have made it on to my list!"
message_3 = f"Congratulations, {names[2].title()}! You have made it on to my list!"

print(message_1)
print(message_2)
print(message_3)

cars = ["honda jazz", "ford ka", "land rover discovery"]

print(f"Unfortunately, I drive a {cars[0].title()}.")
print(f"I won't let Mike drive a {cars[1].title()}.")
print(
    f"When I was a child, I desperately wanted to own a {cars[2].title()} when I grew up."
)
