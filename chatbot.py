from prompt_filter import analyze_prompt, log_attempt
from safe_response import generate_response

def main():
    print("=== PromptShield Secure Chatbot ===")
    print("Type 'exit' to quit.\n")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        malicious, reason = analyze_prompt(user)
        if malicious:
            log_attempt(user, reason)
            print(f"Bot: Request blocked — {reason}. This attempt has been logged.")

            continue

        reply = generate_response(user)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    main()
