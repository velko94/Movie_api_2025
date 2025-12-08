import db_connection
import variables


def ranglist_menu():
    print(
        "choices are:\n rate - list top rated movies according to imdb "
        "\n newest - list the newest by the year of release "
        " \n liked - list top rated in a specific genre "
        "\n lv - leave menu")
    ranglist_engine()


def ranglist_engine():
    while True:
        choice = input("What do you want to do in the ranglist menu ", ).strip().lower()

        if choice == 'rate':
            print("Want to list movies by rating")
            rang_rated()

        elif choice == "newest":
            print("Want to see the newest movies")
            rang_newest()

        elif choice == 'liked':
            print("So you want to list most liked movies in a genre")
            rang_liked()
            continue

        elif choice == 'lv':
            print("leave menu")
            return

        else:
            variables.wrong_choice()
            print("choices are rate,newest,liked")
            continue


def rang_rated():
    conn, cur = db_connection.get_connection()
    cur.execute("SELECT MOVIE_TITLE , LIKENESS FROM movie ORDER BY LIKENESS DESC LIMIT 5 ;")
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()


def rang_liked():
    conn, cur = db_connection.get_connection()
    ranged = variables.input_genre()
    cur.execute("SELECT MOVIE_TITLE,GENRE,LIKENESS FROM movie WHERE GENRE LIKE ? ORDER BY LIKENESS DESC LIMIT 5;",
                ['%' + ranged + '%'])
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()


def rang_newest():
    conn, cur = db_connection.get_connection()
    cur.execute("SELECT ID,MOVIE_TITLE, RELEASE_YEAR FROM movie ORDER BY RELEASE_YEAR DESC LIMIT 5 ;")
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()
