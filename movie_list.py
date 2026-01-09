from pprint import pprint


def list_of_movies():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    print("Here is what we have stored in the library")
    cur.execute('SELECT MOVIE_NAME FROM movie GROUP BY ID')
    pprint(cur.fetchall())


def list_of_movies_admin():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    print("Here is what we have stored in the library")
    cur.execute('SELECT ID, MOVIE_NAME FROM movie GROUP BY ID')
    pprint(cur.fetchall())
