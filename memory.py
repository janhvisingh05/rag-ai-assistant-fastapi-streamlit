def format_history(history):
    formatted = ""
    for q, a in history:
        formatted += f"User: {q}\nAssistant: {a}\n"
    return formatted