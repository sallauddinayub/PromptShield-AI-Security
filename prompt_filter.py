import re
from datetime import datetime

# 🔢 Attack counter (NEW)
ATTACK_COUNT = 0

ROLE_MANIPULATION = [
    r"\bignore (all )?instructions\b",
    r"\bact as\b",
    r"\bpretend\b",
    r"\byou are now\b",
    r"\bdeveloper mode\b",
]

SENSITIVE = [
    r"\bpassword\b",
    r"\badmin\b",
    r"\btoken\b",
    r"\bapikey\b",
    r"\bapi key\b",
    r"\bcredentials?\b",
    r"\bconfidential\b",
    r"\bsecret\b",
]

JAILBREAK = [
    r"\bdo anything now\b",
    r"\bDAN\b",
    r"\bsimulate being\b",
    r"\bhypothetical scenario\b",
    r"\bbypass safety\b",
]

LOG_FILE = "security_log.txt"


def _match_any(patterns, text):
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            return p
    return None


def analyze_prompt(text: str):
    """Return (is_malicious: bool, reason: str)"""
    if _match_any(ROLE_MANIPULATION, text):
        return True, "Role manipulation pattern"
    if _match_any(SENSITIVE, text):
        return True, "Sensitive data request"
    if _match_any(JAILBREAK, text):
        return True, "Jailbreak pattern"
    return False, ""


def log_attempt(text: str, reason: str):
    global ATTACK_COUNT
    ATTACK_COUNT += 1

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (
        f"[WARNING] Prompt Injection Attempt | Time: {ts}\n"
        f"Input: {text}\n"
        f"Reason: {reason}\n"
        f"Total Blocked Attacks: {ATTACK_COUNT}\n\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

    # 🔔 Real-time alert in console
    print(f"[ALERT] Total blocked attacks so far: {ATTACK_COUNT}")
