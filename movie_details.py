from db_connection import get_connection
from variables import wrong_choice, check_output, name


def details():
    detail = input("Do you know the name or the ID of the movie ").strip().lower()
    if len(detail) == 0:
        wrong_choice()
        details()
    elif detail == 'id':
        conn, cur = get_connection()  # from db connections
        detail_id = input("What is the id of the movie ").strip().lower()
        if detail_id.isdigit():
            int(detail_id)
            cur.execute(
                "SELECT MOVIE_TITLE,GENRE,DIRECTOR,DESCRIPTION,RELEASE_YEAR,LIKENESS FROM movie WHERE ID=?;",
                [detail_id])
            results = cur.fetchall()
            check_output(results)  # called from variables
        else:
            print("Please input correct id")
            details()
    elif detail == 'name':
        conn, cur = get_connection()
        detail_name = name()  # called from variables name
        cur.execute(
            "SELECT MOVIE_TITLE, DESCRIPTION, RELEASE_YEAR, DIRECTOR, GENRE, LIKENESS "
            "FROM movie WHERE MOVIE_TITLE LIKE ?;",
            ["%" + detail_name + "%"])
        results = cur.fetchall()
        check_output(results)  # called from variables
        conn.close()
    else:
        print("Please type name or id")
        details()
