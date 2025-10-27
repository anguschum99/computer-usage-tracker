# tracker/db.py
import sqlite3
from datetime import datetime

DB_NAME = "usage_data.db"

def init_db():
    """Creates the SQLite database and table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT,
            window_title TEXT,
            start_time TEXT,
            end_time TEXT,
            duration REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_activity(app_name, window_title, start_time, end_time):
    """Inserts a single activity record into the database."""
    if not app_name:
        return

    duration = (end_time - start_time).total_seconds()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO activity_log (app_name, window_title, start_time, end_time, duration)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        app_name,
        window_title,
        start_time.isoformat(),
        end_time.isoformat(),
        duration
    ))
    conn.commit()
    conn.close()
