from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)


def get_response(message):
    message = message.lower().strip()

    # Greeting
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you!",
            "Hey! Welcome to TechNova Chatbot!"
        ])

    # Positive feedback
    elif any(phrase in message for phrase in [
        "good", "great", "excellent", "working very well",
        "you are helpful", "well done", "awesome"
    ]):
        return "Thank you! 😊 I'm happy to help you."

    # Chatbot name
    elif "your name" in message or "who are you" in message:
        return "My name is TechNova Chatbot."

    # Capabilities
    elif "help" in message or "what can you do" in message:
        return (
            "I can answer questions about Python, AI, programming, "
            "college, studying, date, and time."
        )

    # Programming
    elif "python" in message or "programming" in message:
        return "Python is a popular programming language used in AI and web development."

    # Artificial Intelligence
    elif "artificial intelligence" in message or " ai " in f" {message} ":
        return "AI helps computers perform tasks that usually require human intelligence."

    # Study advice
    elif any(word in message for word in ["study", "exam", "studying"]):
        return "Create a timetable, practise daily, and revise regularly."

    # College
    elif "college" in message or "student" in message:
        return "College is a great place to learn skills and build projects."

    # Date
    elif "date" in message or "today" in message:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    # Time
    elif "time" in message:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Thanks
    elif "thank" in message:
        return "You're welcome! Happy to help."

    # Farewell
    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    # Fallback
    else:
        return (
            "I'm still learning! Try asking me about Python, AI, "
            "college, studying, the date, or the time."
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message."}), 400

    reply = get_response(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)