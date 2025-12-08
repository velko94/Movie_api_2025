import db_connection
import variables


def details():
    while True:
        detail = input("Do you know the name or the ID of the movie ").strip().lower()

        if len(detail) == 0:
            variables.wrong_choice()
            continue

        elif detail == 'id':
            conn, cur = db_connection.get_connection()
            detail_id = input("What is the id of the movie ")

            if detail_id.isdigit():
                cur.execute(
                    "SELECT MOVIE_TITLE,GENRE,DIRECTOR,DESCRIPTION,RELEASE_YEAR,LIKENESS FROM movie WHERE ID=?;",
                    [detail_id])
                results = cur.fetchall()
                conn.close()

                variables.check_output(results)
                return
            else:
                print("Please input correct id")
                continue

        elif detail == 'name':
            detail_name = variables.name()

            conn, cur = db_connection.get_connection()
            cur.execute(
                "SELECT MOVIE_TITLE, DESCRIPTION, RELEASE_YEAR, DIRECTOR, GENRE, LIKENESS "
                "FROM movie WHERE MOVIE_TITLE LIKE ?;",
                ["%" + detail_name + "%"])
            results = cur.fetchall()
            conn.close()

            variables.check_output(results)
            return
        else:
            print("Please type name or id")
    return
