import db_connection
import variables


def search_menu():
    print(
        "options to search by are:""\n name -  The movie's name,"
        " \n genre - The genre of the movie, "
        "\n desc -  Some of the description,"
        "\n dir - Name of the director,"
        " \n year -  The year it was released")
    search_engine()


def search_engine():
    while True:
        search_by = input("please choose by what parameter to search for ").strip().lower()
        conn, cur = db_connection.get_connection()

        if search_by == 'name':
            search_parameter = variables.name()
            cur.execute(
                "SELECT * FROM movie WHERE MOVIE_TITLE LIKE ?;",
                ["%" + search_parameter + "%", ])
            results = cur.fetchall()
            variables.check_output(results)
            conn.close()
            break

        elif search_by == 'genre':
            search_parameter = variables.input_genre()
            cur.execute(
                "SELECT * FROM movie WHERE GENRE LIKE ?;",
                ["%" + search_parameter + "%"])
            results = cur.fetchall()
            variables.check_output(results)
            conn.close()
            break

        elif search_by == 'desc':
            search_parameter = variables.description()
            cur.execute(
                "SELECT *  FROM movie WHERE DESCRIPTION LIKE ? ;",
                ["%" + search_parameter + "%"])
            results = cur.fetchall()
            variables.check_output(results)
            conn.close()
            break

        elif search_by == 'dir':
            search_parameter = variables.director_name()
            cur.execute(
                "SELECT * FROM movie WHERE DIRECTOR LIKE ? ;",
                ["%" + search_parameter + "%"])
            results = cur.fetchall()
            variables.check_output(results)
            conn.close()
            break

        elif search_by == 'year':
            search_parameter = variables.release_year()
            cur.execute(
                "SELECT * FROM movie WHERE RELEASE_YEAR = ?  ;",
                [search_parameter])
            results = cur.fetchall()
            variables.check_output(results)
            conn.close()
            break

        else:
            print("Please use the parameters name,genre,desc,dir,year")
            variables.wrong_choice()
            conn.close()
            continue
