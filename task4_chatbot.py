from datetime import datetime

print("=" * 35)
print("       Smart Python Chatbot")
print("Type 'help' for commands.")
print("Type 'bye' to exit.")
print("=" * 35)

name = input("Before we start, what's your name? ")

print(f"Bot: Nice to meet you, {name}!\n")

while True:
    user = input(f"{name}: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print(f"Bot: Hello {name}! ")

    # How are you
    elif user in ["how are you", "how are you?"]:
        print("Bot: I'm doing great. Thanks for asking! ")

    # Name
    elif user in ["what is your name", "who are you"]:
        print("Bot: I am SmartBot, created using Python.")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Date
    elif user == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    # Help
    elif user == "help":
        print("""
Available Commands:
- hello / hi / hey
- how are you
- what is your name
- time
- date
- help
- bye
        """)

    # Bye
    elif user == "bye":
        print(f"Bot: Goodbye, {name}! Have a nice day. ")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")