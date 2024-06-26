# Exercise 3-4
guest_list = ["John Lennon", "Voltaire", "Steve Coogan"]

print(f"Dear {guest_list[0]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[1]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[2]}, You are cordially invited to join me for dinner.")

# Exercise 3-5
# John can't make it
print("John Lennon")

# So I'm inviting Gruff Rhys instead
guest_list[0] = "Gruff Rhys"

print(f"Dear {guest_list[0]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[1]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[2]}, You are cordially invited to join me for dinner.")


# Exercise 3-6
print(
    "Hi all, Just to let you know that I've found a bigger table so I'm able to invite more people!"
)

guest_list.insert(0, "Jarvis Cocker")
guest_list.insert(3, "Susan Kennedy")
guest_list.append("Karl Kennedy")

print(f"Dear {guest_list[0]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[1]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[2]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[3]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[4]}, You are cordially invited to join me for dinner.")
print(f"Dear {guest_list[5]}, You are cordially invited to join me for dinner.")

# Exercise 3-7
print(
    "Sorry guys, my table won't arrive in time so I can only have two people over for dinner."
)

uninvited_1 = guest_list.pop()
print(
    f"Really sorry, {uninvited_1}, but I haven't got room for you at my dinner party anymore."
)
uninvited_2 = guest_list.pop()
print(
    f"Really sorry, {uninvited_2}, but I haven't got room for you at my dinner party anymore."
)
uninvited_3 = guest_list.pop()
print(
    f"Really sorry, {uninvited_3}, but I haven't got room for you at my dinner party anymore."
)
uninvited_4 = guest_list.pop()
print(
    f"Really sorry, {uninvited_4}, but I haven't got room for you at my dinner party anymore."
)

print(f"Hi {guest_list[0]} - just letting you know you're still invited to dinner.")
print(f"Hi {guest_list[1]} - just letting you know you're still invited to dinner.")


del guest_list[1]
del guest_list[0]

print(f"guest_list is now {guest_list}")
