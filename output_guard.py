def validate_output(response):
    print("\n[OUTPUT GUARD] Checking model response...")

    if not response or len(response.strip()) < 5:
        print("[OUTPUT GUARD] ❌ Rejected: Empty or too short")
        return False

    unsafe_phrases = [
        "i don't know",
        "not sure",
        "cannot answer",
        "no information available"
    ]

    for phrase in unsafe_phrases:
        if phrase in response.lower():
            print(f"[OUTPUT GUARD] ❌ Rejected: Weak response detected -> {phrase}")
            return False

    print("[OUTPUT GUARD] ✅ Passed")
    return True