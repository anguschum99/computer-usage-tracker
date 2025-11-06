# dashboard_api.py
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "usage_data.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    conn.close()
    return (rows[0] if rows else None) if one else rows

@app.route("/api/usage")
def get_usage_data():
    rows = query_db("""
        SELECT app_name, ROUND(SUM(duration)/60, 2) AS total_minutes
        FROM activity_log
        GROUP BY app_name
        ORDER BY total_minutes DESC;
    """)
    data = [dict(row) for row in rows]
    return jsonify(data)

@app.route("/api/raw")
def get_raw_data():
    rows = query_db("""
        SELECT id, app_name, window_title, duration, start_time, end_time
        FROM activity_log
        ORDER BY id DESC LIMIT 50;
    """)
    data = [dict(row) for row in rows]
    return jsonify(data)

if __name__ == "__main__":
    print("🚀 Dashboard API running at http://127.0.0.1:5000")
    app.run(debug=True)
