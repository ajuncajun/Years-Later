# db.py
import sqlite3

DB_NAME = "trip_planner.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # returns dict-like rows
    return conn
