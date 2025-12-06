import variables
from db_connection import get_connection


def ranglist_menu():
    print(
        "choices are:\n rate - list top rated movies according to imdb "
        "\n newest - list the newest by the year of release "
        " \n liked - list top rated in a specific genre ")
    ranglist_engine()


def ranglist_engine():
    choice = input("What do you want to do ", ).strip().lower()
    if choice == 'rate':
        print("Want to list movies by rating")
        rang_rated()
    elif choice == "newest":
        print("Want to see the newest movies")
        rang_newest()
    elif choice == 'liked':
        print("So you want to list most liked movies in a genre")
        variables.input_genre()
        rang_liked()
    else:
        variables.wrong_choice()
        print("choices are rate,newest,liked")
        ranglist_engine()


def rang_rated():
    conn, cur = get_connection()
    cur.execute("SELECT MOVIE_TITLE , LIKENESS FROM movie ORDER BY LIKENESS DESC LIMIT 5 ;")
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()


def rang_liked():
    conn, cur = get_connection()
    ranged = variables.genre
    cur.execute("SELECT MOVIE_TITLE,GENRE,LIKENESS FROM movie WHERE GENRE LIKE ? ORDER BY LIKENESS DESC LIMIT 5;",
                ['%' + ranged + '%'])
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()


def rang_newest():
    conn, cur = get_connection()
    cur.execute("SELECT ID,MOVIE_TITLE, RELEASE_YEAR FROM movie ORDER BY RELEASE_YEAR DESC LIMIT 5 ;")
    results = cur.fetchall()
    variables.check_output(results)
    conn.close()
