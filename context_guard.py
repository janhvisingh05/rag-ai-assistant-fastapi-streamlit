def is_context_relevant(context):
    print("\n[CONTEXT GUARD] Checking retrieved context...")

    if not context:
        print("[CONTEXT GUARD] ❌ Rejected: No context retrieved")
        return False

    if len(context.strip()) < 20:
        print("[CONTEXT GUARD] ❌ Rejected: Context too weak")
        return False

    print("[CONTEXT GUARD] ✅ Passed")
    return True