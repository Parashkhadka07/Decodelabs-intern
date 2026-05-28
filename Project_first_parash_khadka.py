# ============================================================
#   Rule-Based AI Chatbot
#   DecodeLabs Industrial Training | Project 1
#   Built by: Parash Khadka
# ============================================================

# ── KNOWLEDGE BASE (O(1) Dictionary Lookup) ──────────────────
responses = {
    # Greetings
    "hello":        "Hey there! I'm DecoBot. How can I assist you today?",
    "hi":           "Hi! Great to see you. What's on your mind?",
    "hey":          "Hey! I'm here and ready. Ask me anything.",

    # Identity
    "who are you":  "I'm DecoBot, a rule-based AI chatbot built by Parash Khadka for DecodeLabs Project 1.",
    "what are you": "I'm a deterministic chatbot — I run on pure logic, no neural networks involved!",
    "your name":    "My name is DecoBot. Nice to meet you!",

    # Wellbeing
    "how are you":  "I'm a program, so I'm always at 100%! How about you?",
    "are you okay": "Fully operational and running smoothly. Thanks for asking!",

    # About AI
    "what is ai":         "AI stands for Artificial Intelligence — machines designed to simulate human-like decision making.",
    "what is ml":         "Machine Learning is a subset of AI where systems learn from data instead of explicit rules.",
    "what is deep learning": "Deep Learning uses multi-layered neural networks to learn complex patterns from large datasets.",
    "difference between ai and ml": "AI is the broad concept; ML is a technique to achieve AI through data-driven learning.",

    # About DecodeLabs
    "what is decodelabs": "DecodeLabs is a tech training organization that helps students build real-world AI projects step by step.",
    "what is project 1":  "Project 1 is the Rule-Based AI Chatbot — your foundation milestone at DecodeLabs.",

    # Fun / Personality
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "motivate me":    "Every expert was once a beginner. Write the first rule, then write a thousand more. You've got this!",
    "what can you do": "I can answer questions, tell jokes, explain AI concepts, and keep you company. Try me!",

    # Farewells
    "bye":       "Goodbye! Keep building. See you next time! 👋",
    "goodbye":   "Take care! Your AI journey is just getting started. 🚀",
    "see you":   "See you soon! Don't forget to commit your code. 😄",

    # Exit hint
    "exit":      "__EXIT__",
    "quit":      "__EXIT__",
}


# ── HELPER: Print with bot prefix ────────────────────────────
def bot_say(message):
    print(f"\n  🤖 DecoBot: {message}\n")


# ── HELPER: Sanitize raw input ───────────────────────────────
def sanitize(raw):
    return raw.lower().strip()


# ── MAIN CHATBOT LOOP ────────────────────────────────────────
def run_chatbot():
    print("=" * 55)
    print("   Welcome to DecoBot — Rule-Based AI Chatbot")
    print("   DecodeLabs Industrial Training | Project 1")
    print("   Type 'exit' or 'quit' to end the session.")
    print("=" * 55)

    while True:
        try:
            raw_input_text = input("\n  You: ")
        except (EOFError, KeyboardInterrupt):
            bot_say("Session interrupted. Goodbye!")
            break

        clean_input = sanitize(raw_input_text)

        # Skip empty input
        if not clean_input:
            bot_say("Please type something. I'm listening!")
            continue

        # Lookup response from knowledge base
        reply = responses.get(clean_input, None)

        # Exit command
        if reply == "__EXIT__":
            bot_say("Goodbye! Keep building amazing things. See you! 👋")
            break

        # Fallback for unknown inputs
        if reply is None:
            bot_say("I don't understand that yet. Try asking about AI, ML, or just say 'hello'!")
        else:
            bot_say(reply)


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()