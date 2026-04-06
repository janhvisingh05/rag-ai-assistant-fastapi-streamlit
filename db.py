import sqlite3

DB_PATH = "database/chat.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    with open("database/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users(username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def get_user_id(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=?", (username,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

def save_chat(user_id, question, answer):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chat_history(user_id, question, answer) VALUES (?, ?, ?)",
        (user_id, question, answer)
    )
    conn.commit()
    conn.close()

def get_chat_history(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT question, answer FROM chat_history WHERE user_id=? ORDER BY id DESC LIMIT 5",
        (user_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows[::-1]