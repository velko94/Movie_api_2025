from db_connection import get_connection
from variables import check_output


def list_of_movies():
    conn, cur = get_connection()
    print("Here is what we have stored in the library")
    cur.execute('SELECT MOVIE_TITLE FROM movie ORDER BY ID')
    results = cur.fetchall()
    check_output(results)  # called from variables
    conn.close()


def list_of_movies_admin():
    conn, cur = get_connection()
    print("Here is what we have stored in the library")
    cur.execute('SELECT ID, MOVIE_TITLE FROM movie ORDER BY ID')
    results = cur.fetchall()
    check_output(results)  # called from variables
    conn.close()
