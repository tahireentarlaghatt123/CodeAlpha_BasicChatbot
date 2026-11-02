
def chatbot():
    print("================================")
    print("       CODEALPHA CHATBOT")
    print("================================")
    print("Bot: Hello! Welcome to my chatbot.")
    print("Bot: Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I am fine! Thank you.")

        elif user_input == "what is your name":
            print("Bot: I am CodeAlpha Chatbot.")

        elif user_input == "help":
            print("Bot: Sure! Tell me what you need.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
