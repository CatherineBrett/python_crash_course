# Exercise 5-8

# usernames = ["catherineb", "michaelb", "elizabeths", "alaindb", "admin"]

# for username in usernames:
#     if username == "admin":
#         print("Hi admin! Would you like to see a status report?")
#     else:
#         print(f"Hello {username}. Welcome back!")


# Exercise 5-9

usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hi admin! Would you like to see a status report?")
        else:
            print(f"Hello {username}. Welcome back!")
else:
    print("We need to find some users!")
