# ==============================
# Basic Rule-Based Chatbot
# ==============================

def chatbot():
    print("Bot: Hello! I am your chatbot 🤖")
    print("Bot: Type 'bye' to exit\n")

    while True:
        user_input = input("You: ").lower()

        # Greeting
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi! 👋")

        # Asking about health
        elif "how are you" in user_input:
            print("Bot: I'm fine, thanks! 😊")

        # Name
        elif "your name" in user_input:
            print("Bot: I am a simple chatbot.")

        # Thanks
        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're welcome! 👍")

        # Goodbye
        elif "bye" in user_input:
            print("Bot: Goodbye! 👋")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand 🤔")

# Run chatbot
chatbot()