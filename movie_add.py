import variables


def adding():

    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    details = variables.user_input()
    cur.execute(
        "INSERT INTO movie (MOVIE_NAME, GENRE, DIRECTOR, DESCRIPTION, RELEASE_YEAR,LIKENESS) VALUES (?,?,?,?,?,?)",
        details)
    conn.commit()
    conn.close()
