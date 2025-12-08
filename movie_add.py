import db_connection
import variables


def adding():
    details = variables.user_input()
    conn, cur = db_connection.get_connection()
    cur.execute(
        "INSERT INTO movie (MOVIE_TITLE, DESCRIPTION, RELEASE_YEAR, DIRECTOR, GENRE, LIKENESS) "
        "VALUES (?,?,?,?,?,?)", details)

    new_id = cur.lastrowid
    cur.execute("SELECT * FROM movie WHERE ID=?", (new_id,))
    added_movie = cur.fetchone()
    print(f"Just added: {added_movie}")
    conn.commit()
    conn.close()
