from db_connection import get_connection
from variables import check_output, name, input_genre, description, director_name, release_year, wrong_choice


def search_menu():
    print(
        "options to search by are:""\n name -  The movie's name,"
        " \n genre - The genre of the movie, "
        "\n desc -  Some of the description,"
        "\n dir - Name of the director,"
        " \n year -  The year it was released")
    search_engine()


def search_engine():
    conn, cur = get_connection()
    search_by = input("please choose by what parameter to search for ").strip().lower()
    if search_by == 'name':
        search_parameter = name()
        cur.execute(
            "SELECT * FROM movie WHERE MOVIE_TITLE LIKE ?;",
            ["%" + search_parameter + "%", ])
        results = cur.fetchall()
        check_output(results)
        conn.close()
    elif search_by == 'genre':
        search_parameter = input_genre()
        cur.execute(
            "SELECT * FROM movie WHERE GENRE LIKE ?;",
            ["%" + search_parameter + "%"])
        results = cur.fetchall()
        check_output(results)
        conn.close()
    elif search_by == 'desc':
        search_parameter = description()
        cur.execute(
            "SELECT *  FROM movie WHERE DESCRIPTION LIKE ? ;",
            ["%" + search_parameter + "%"])
        results = cur.fetchall()
        check_output(results)
        conn.close()
    elif search_by == 'dir':
        search_parameter = director_name()
        cur.execute(
            "SELECT * FROM movie WHERE DIRECTOR LIKE ? ;",
            ["%" + search_parameter + "%"])
        results = cur.fetchall()
        check_output(results)
        conn.close()
    elif search_by == 'year':
        search_parameter = release_year()
        cur.execute(
            "SELECT * FROM movie WHERE RELEASE_YEAR = ?  ;",
            [search_parameter])
        results = cur.fetchall()
        check_output(results)
        conn.close()
    else:
        print("Please use the parameters name,genre,desc,dir,year")
        wrong_choice()
        search_engine()
