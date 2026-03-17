while True:
    msg = input("You: ").lower()
    if "hi" in msg:
        print("Bot: Hello!")
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
