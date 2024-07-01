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

# Exercise 3-9
print(
    f"The length of my guest list before I start uninviting everyone is {len(guest_list)}."
)

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

# Exercise 3-8
places_to_visit = ["cannes", "ibiza", "australia", "new zealand", "canada"]
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# Exercise 3-10
my_languages = ["english", "french", "spanish", "italian"]
print("Exercise 3-10")
print(my_languages)
print(f"My native language is {my_languages[0].title()}")
print(f"The language I started learning most recently is {my_languages[-1].title()}")
print(f"The language I started learning before that was {my_languages[-2].title()}")
my_languages[0] = "gibberish"
print(my_languages)
my_languages.append("ukrainian")
print(my_languages)
my_languages = []
print(f"my_languages = {my_languages}")
my_languages.append("english")
my_languages.append("french")
my_languages.append("spanish")
my_languages.append("italian")
print(my_languages)
my_languages.insert(1, "gibberish")
print(my_languages)
del my_languages[1]
print(my_languages)
most_recent_language = my_languages.pop()
print(my_languages)
print(most_recent_language)
print(f"The language I began learning most recently is {most_recent_language.title()}.")
first_language = my_languages.pop(0)
print(my_languages)
print(first_language)
print(
    f"My native language, aka the first language I ever learned, is {first_language.title()}."
)
my_languages.remove("spanish")
print(my_languages)
remaining_language = "french"
my_languages.remove(remaining_language)
print(my_languages)
print(
    f"Now that I have used the remove() method to remove {remaining_language.title()} from the list, the my_languages list now looks like this: {my_languages}"
)
my_languages = ["french", "spanish", "italian", "french"]
print(my_languages)
occurrence = "french"
my_languages.remove(occurrence)
print(my_languages)
print(
    f"The value '{occurrence}' occurred both at the beginning and the end of the list, but the remove() method only deletes the first occurrence of something, so the updated list looks like this: {my_languages}."
)
my_languages.sort()
print(my_languages)
my_languages.sort(reverse=True)
print(my_languages)
some_languages = ["welsh", "arabic", "punjabi"]
print(f"Here is the original some_languages list: {some_languages}")
print(f"Here is the sorted (alphabetical) version: {sorted(some_languages)}")
print(
    f"Here is the reverse-alphabetical version: {sorted(some_languages, reverse=True)}"
)
print(
    f"And here is the original list again: {some_languages}. The sorted() function displayed it alphabetically (and then in reverse) for me, but didn't affect the order of the actual list."
)
cities = ["london", "paris", "madrid", "rome"]
print(cities)
cities.reverse()
print(cities)
cities.reverse()
print(cities)
print(f"There are {len(cities)} cities in my list.")
