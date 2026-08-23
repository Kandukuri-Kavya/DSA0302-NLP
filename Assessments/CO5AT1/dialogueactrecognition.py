dialogue = [
    ("User", "Can you book a train ticket for me?"),
    ("Agent", "Sure, where would you like to travel?"),
    ("User", "I want to go to Chennai."),
    ("Agent", "Your ticket has been booked.")
]

for speaker, text in dialogue:
    if "book" in text.lower() and "?" in text:
        act = "Request"
    elif "where" in text.lower():
        act = "Question"
    elif "want to go" in text.lower():
        act = "Inform"
    else:
        act = "Confirmation/Action"

    print(speaker, ":", act)