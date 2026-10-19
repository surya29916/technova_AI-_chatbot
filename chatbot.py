import random
from datetime import datetime

# TechNova Rule-Based Chatbot
print("=" * 45)
print("       Welcome to TechNova Chatbot!")
print("=" * 45)
print("Hello! I am your chatbot assistant.")
print("Type 'bye' to exit.\n")

# Chatbot responses for different intents
responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi there! Nice to meet you!",
        "Hey! What can I do for you?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you soon!",
        "Thank you for chatting with me!"
    ],
    "name": [
        "My name is TechNova Chatbot.",
        "You can call me TechNova."
    ],
    "creator": [
        "I was created using Python and rule-based logic."
    ],
    "help": [
        "I can answer questions about greetings, studying, "
        "Python, college, and more."
    ],
    "study": [
        "Make a timetable and practise every day.",
        "Study in small sessions and revise regularly."
    ],
    "python": [
        "Python is a popular programming language.",
        "You can use Python for AI, machine learning, and web development."
    ],
    "ai": [
        "Artificial Intelligence helps computers perform tasks "
        "that normally require human intelligence."
    ],
    "college": [
        "College is a great place to learn, practise, and build projects."
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!"
    ],
    "time": [
        f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    ],
    "date": [
        f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."
    ]
}


def get_response(message):
    message = message.lower().strip()

    # Greeting
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])

    # Goodbye
    elif any(word in message for word in ["bye", "goodbye", "exit"]):
        return random.choice(responses["goodbye"])

    # Name
    elif "your name" in message or "who are you" in message:
        return random.choice(responses["name"])

    # Creator
    elif "created you" in message or "who made you" in message:
        return random.choice(responses["creator"])

    # Help
    elif "help" in message or "what can you do" in message:
        return random.choice(responses["help"])

    # Study
    elif any(word in message for word in ["study", "exam", "studying"]):
        return random.choice(responses["study"])

    # Python
    elif "python" in message or "programming" in message:
        return random.choice(responses["python"])

    # Artificial Intelligence
    elif "artificial intelligence" in message or " ai " in f" {message} ":
        return random.choice(responses["ai"])

    # College
    elif "college" in message or "student" in message:
        return random.choice(responses["college"])

    # Thanks
    elif "thank" in message or "thanks" in message:
        return random.choice(responses["thanks"])

    # Time
    elif "time" in message:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Date
    elif "date" in message or "today" in message:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    # Fallback response
    else:
        return "Sorry, I don't understand that yet. Try asking me for help."


# Main chatbot loop
while True:
    user_input = input("You: ")
    reply = get_response(user_input)
    print("TechNova Bot:", reply)

    if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
        break