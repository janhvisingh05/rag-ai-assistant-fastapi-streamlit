import streamlit as st
import datetime

from database.db import init_db, create_user, get_user_id, save_chat, get_chat_history
from rag.retriever import retrieve_context
from llm.langchain_gemini import generate_response
from utils.memory import format_history

# GUARDRAILS
from guardrails.input_guard import is_safe_input
from guardrails.context_guard import is_context_relevant
from guardrails.output_guard import validate_output

# -------------------------------
# INIT
# -------------------------------
init_db()

st.set_page_config(page_title="AI Assistant", layout="wide")
st.title("AI Assistant (RAG + Memory + Guardrails)")

# -------------------------------
# TERMINAL LOGGER
# -------------------------------
def log_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)

def log_chat(question, answer, context):
    print("\n" + "="*70)
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    print("\n[USER QUESTION]")
    print(question)

    print("\n[RETRIEVED CONTEXT - TOP CHUNKS]")
    print(context[:800])

    print("\n[FINAL RESPONSE]")
    print(answer)

    print("="*70 + "\n")


# -------------------------------
# USER INPUT
# -------------------------------
username = st.text_input("Enter username")

if username:
    create_user(username)
    user_id = get_user_id(username)

    st.success(f"Logged in as: {username}")

    question = st.text_input("Ask something about your documents")

    if question:

        log_section("🚀 NEW QUERY START")
        print(f"[USER INPUT] {question}")

        # -------------------------------
        # INPUT GUARDRAIL
        # -------------------------------
        print("\n[INPUT GUARD] Checking input...")
        is_safe, msg = is_safe_input(question)

        if not is_safe:
            print(f"[INPUT GUARD] ❌ FAILED: {msg}")
            st.error(msg)
            st.stop()
        else:
            print("[INPUT GUARD] ✅ PASSED")

        with st.spinner("Thinking..."):

            # -------------------------------
            # MEMORY
            # -------------------------------
            print("\n[MEMORY] Fetching chat history...")
            history = get_chat_history(user_id)
            formatted_history = format_history(history)

            print("[MEMORY] Formatted history:")
            print(formatted_history if formatted_history else "No history")

            # -------------------------------
            # RETRIEVE CONTEXT
            # -------------------------------
            print("\n[RETRIEVER] Fetching context...")
            context = retrieve_context(question)

            print("[RETRIEVER] Context preview:")
            print(context[:300] if context else "No context retrieved")

            # -------------------------------
            # CONTEXT GUARDRAIL
            # -------------------------------
            print("\n[CONTEXT GUARD] Checking relevance...")
            if not is_context_relevant(context):
                print("[CONTEXT GUARD] ❌ FAILED: Context not relevant")
                st.warning("Not enough relevant information found.")
                st.stop()
            else:
                print("[CONTEXT GUARD] ✅ PASSED")

            # -------------------------------
            # GENERATE RESPONSE
            # -------------------------------
            print("\n[LLM] Generating response...")
            answer = generate_response(context, question, formatted_history)

            print("\n[LLM OUTPUT]")
            print(answer)

            # -------------------------------
            # OUTPUT GUARDRAIL
            # -------------------------------
            print("\n[OUTPUT GUARD] Checking response...")
            if not validate_output(answer):
                print("[OUTPUT GUARD] ❌ FAILED: Unsafe/low-quality response")
                answer = "Response blocked due to safety constraints."
            else:
                print("[OUTPUT GUARD] ✅ PASSED")

            # -------------------------------
            # SAVE CHAT
            # -------------------------------
            print("\n[DATABASE] Saving chat...")
            save_chat(user_id, question, answer)
            print("[DATABASE] ✅ Saved")

            # -------------------------------
            # FINAL LOG
            # -------------------------------
            log_chat(question, answer, context)

        # -------------------------------
        # UI OUTPUT
        # -------------------------------
        st.markdown("## 🧠 Answer")
        st.write(answer)

        # -------------------------------
        # CHAT HISTORY
        # -------------------------------
        st.markdown("## 💬 Chat History")

        if history:
            for q, a in history:
                st.markdown(f"**You:** {q}")
                st.markdown(f"**Bot:** {a}")
                st.markdown("---")
        else:
            st.info("No previous chat history found.")