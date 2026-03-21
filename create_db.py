import sqlite3

def create_tables():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # ================= USERS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # ================= NOTES =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        subject TEXT,
        content TEXT
    )
    """)

    # ================= STUDY PLAN =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS study_plan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        topic TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)

    # ================= ANALYTICS =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS analytics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        topic TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print("✅ All tables created successfully")


# 🔥 RUN FILE
if __name__ == "__main__":
    create_tables()