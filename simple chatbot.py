"""
Rule-Based Chatbot
------------------
Handles greetings and exit commands using if-else logic in a continuous loop.

How to run:
    python simple_chatbot.py
"""

print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hi there! How can I help you today?")

    elif user_input in ["how are you", "how are you?"]:
        print("Chatbot: I'm doing great, thanks for asking!")

    elif user_input in ["what is your name", "what is your name?", "who are you"]:
        print("Chatbot: I'm Chatty, a simple rule-based chatbot.")

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that. Can you rephrase?")
