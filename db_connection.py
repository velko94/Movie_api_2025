import sqlite3


def get_connection():
    conn = sqlite3.connect("Movie.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()
    return conn, cur
