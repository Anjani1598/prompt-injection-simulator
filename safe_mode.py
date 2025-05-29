DANGEROUS_PATTERNS = [
    "ignore previous instructions",
    "pretend you're",
    "bypass safety",
    "you are free now",
    "override rules"
]

def is_safe(prompt: str) -> bool:
    prompt_lower = prompt.lower()
    return not any(pattern in prompt_lower for pattern in DANGEROUS_PATTERNS)
