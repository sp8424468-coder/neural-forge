from app import app, get_db

with app.app_context():
    db = get_db()
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS study_plan(
        user TEXT,
        topic TEXT,
        status TEXT
    )
    """)

    db.commit()

print("✅ study_plan table created successfully")