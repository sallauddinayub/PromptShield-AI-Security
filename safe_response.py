def generate_response(user_text: str) -> str:
    text = user_text.lower()

    # Simple FAQ-like responses
    if "hello" in text or "hi" in text:
        return "Hello! How can I assist you today?"
    if "what is ai" in text:
        return "AI stands for Artificial Intelligence — systems that perform tasks requiring human-like intelligence."
    if "help" in text:
        return "I can answer basic questions about technology and learning resources."
    if "cybersecurity" in text:
        return "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks."

    # Default
    return "Thanks for your question! I'm a demo assistant with safety filters enabled."
