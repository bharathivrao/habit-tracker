import os
import sqlite3
from pathlib import Path

DB_PATH = Path("data/habits.db")

def get_db_path():
    return Path(os.environ.get("HABIT_TRACKER_DB") or DB_PATH)

def get_db_connection():
    db_path = get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL
        )
    ''')

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status INTEGER NOT NULL,
            UNIQUE(habit_id, date),
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    """)
    conn.commit()
    conn.close()