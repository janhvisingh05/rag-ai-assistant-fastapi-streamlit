def is_safe_input(user_input):
    print("\n[INPUT GUARD] Checking user input...")

    if not user_input or len(user_input.strip()) < 3:
        print("[INPUT GUARD] ❌ Rejected: Input too short")
        return False, "Input too short"

    unsafe_keywords = ["hack", "exploit", "attack", "illegal"]

    for word in unsafe_keywords:
        if word in user_input.lower():
            print(f"[INPUT GUARD] ❌ Rejected: Unsafe keyword -> {word}")
            return False, f"Unsafe keyword detected: {word}"

    print("[INPUT GUARD] ✅ Passed")
    return True, "Safe"