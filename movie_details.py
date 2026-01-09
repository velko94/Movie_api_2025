import variables
from pprint import pprint


def details():
    detail = str(input("Do you know the name or the ID of the movie "))
    if len(detail) == 0:
        variables.wrong_choice()
        details()
    elif detail == 'id':
        import sqlite3
        conn = sqlite3.connect("Movie.db")
        cur = conn.cursor()
        detail_id = int(input("What is the id of the movie "))
        cur.execute(
            "SELECT MOVIE_NAME,GENRE,DIRECTOR,DESCRIPTION,RELEASE_YEAR,LIKENESS FROM movie WHERE ID=?;", [detail_id])
        pprint(cur.fetchall())
    elif detail == 'name':
        import sqlite3
        conn = sqlite3.connect("Movie.db")
        cur = conn.cursor()
        detail_name = str(input("What is the name of the movie "))
        cur.execute(
            "SELECT MOVIE_NAME,GENRE,DIRECTOR,DESCRIPTION,RELEASE_YEAR,LIKENESS FROM movie WHERE MOVIE_NAME LIKE ?;",
            ["%" + detail_name + "%"])
        pprint(cur.fetchall())
    else:
        print("Wrong answer")
        details()
