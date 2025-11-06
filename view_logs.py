import sqlite3

conn = sqlite3.connect("usage_data.db")
cursor = conn.cursor()

cursor.execute("SELECT id, app_name, window_title, duration FROM activity_log ORDER BY id DESC LIMIT 10;")
rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]:.2f}s")

conn.close()
