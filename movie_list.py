import variables
import db_connection


def list_of_movies():
    conn, cur = db_connection.get_connection()
    print("Here is what we have stored in the library")
    cur.execute('SELECT MOVIE_TITLE FROM movie ORDER BY ID')
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()


def list_of_movies_admin():
    conn, cur = db_connection.get_connection()
    print("Here is what we have stored in the library")
    cur.execute('SELECT ID, MOVIE_TITLE FROM movie ORDER BY ID')
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()
