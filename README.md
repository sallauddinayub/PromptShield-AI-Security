# PromptShield — LLM Prompt Injection Detection System

A simple, beginner-friendly project that demonstrates **AI Security** by protecting a chatbot from prompt injection attacks.

## Features
- Detects role manipulation (e.g., "ignore instructions", "act as admin")
- Detects sensitive data requests (passwords, tokens, credentials)
- Detects jailbreak patterns (DAN, bypass safety, hypothetical scenario)
- Blocks malicious prompts and logs them to `security_log.txt`

## How to Run

1. Make sure you have Python 3.9+ installed.
2. Open a terminal in this folder.
3. Run the chatbot:
   ```bash
   python chatbot.py
   ```

4. (Optional) Run attack simulations:
   ```bash
   python attack_tests.py
   ```

## Project Structure
```
PromptShield/
├── chatbot.py
├── prompt_filter.py
├── safe_response.py
├── attack_tests.py
├── security_log.txt
└── README.md
```

