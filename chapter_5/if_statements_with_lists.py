# Exercise 5-8

# usernames = ["catherineb", "michaelb", "elizabeths", "alaindb", "admin"]

# for username in usernames:
#     if username == "admin":
#         print("Hi admin! Would you like to see a status report?")
#     else:
#         print(f"Hello {username}. Welcome back!")


# Exercise 5-9

# usernames = []

# if usernames:
#     for username in usernames:
#         if username == "admin":
#             print("Hi admin! Would you like to see a status report?")
#         else:
#             print(f"Hello {username}. Welcome back!")
# else:
#     print("We need to find some users!")


# Exercise 5-10

current_users = ["caln", "Georges", "craigb", "michelb", "WendyP", "John"]
new_users = ["georges", "gorev", "bertrandr", "wendyp", "markh", "JOHN"]

current_users_copy = []
for current_user in current_users:
    current_user_lower = current_user.lower()
    current_users_copy.append(current_user_lower)

new_users_copy = []
for new_user in new_users:
    new_user_lower = new_user.lower()
    new_users_copy.append(new_user_lower)

for username in new_users_copy:
    if username in current_users_copy:
        print("Username not available. Please enter a new username.")
    else:
        print("Username available.")
