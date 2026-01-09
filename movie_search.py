import variables
from pprint import pprint


def search_engine():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    print(
        "options to search by are:""\n 1) The movie's name,"
        " \n 2) The genre of the movie, "
        "\n 3) Some of the description,"
        "\n 4) Name of the director,"
        " \n 5) The year it was released")
    search_by = input("please choose by what parameter to search for please use only digits ")
    if search_by == '1':
        search_parameter = variables.name()
        cur.execute(
            "SELECT * FROM movie WHERE MOVIE_NAME LIKE ?;",
            ["%" + search_parameter + "%", ])
        pprint(cur.fetchall())
        conn.close()

    elif search_by == '2':
        search_parameter = variables.input_genre()
        cur.execute(
            "SELECT * FROM movie WHERE GENRE LIKE ?;",
            ["%" + search_parameter + "%"])
        pprint(cur.fetchall())
        conn.close()
    elif search_by == '3':
        search_parameter = variables.description()
        cur.execute(
            "SELECT *  FROM movie WHERE DESCRIPTION LIKE ? ;",
            ["%" + search_parameter + "%"])
        pprint(cur.fetchall())
        conn.close()
    elif search_by == '4':
        search_parameter = variables.director_name()
        cur.execute(
            "SELECT * FROM movie WHERE DIRECTOR LIKE ? ;",
            ["%" + search_parameter + "%"])
        pprint(cur.fetchall())
        conn.close()
    elif search_by == '5':
        search_parameter = variables.release_year()
        cur.execute(
            "SELECT * FROM movie WHERE RELEASE_YEAR=?  ;",
            [search_parameter])
        pprint(cur.fetchall())
        conn.close()
    else:
        variables.wrong_choice()
        search_engine()
