# Exercise 8-9


# def show_messages(list_of_messages):
#     """Prints each message in the list."""
#     for message in list_of_messages:
#         print(message)


# text_messages = ["many thanks", "let me know", "see you then"]

# show_messages(text_messages)


# Exercise 8-10


def send_messages(unsent_messages, sent_messages):
    """Prints each message in the first list and then moves it to a list of
    sent messages."""
    while unsent_messages:
        current_msg = unsent_messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)


unsent = ["many thanks", "let me know", "see you then"]
sent = []

send_messages(unsent, sent)

print(
    f"After calling the function, my 'unsent' list now looks like " f"this: {unsent}."
)
print(f"And my 'sent' list looks like this: {sent}.")
