from pprint import pprint

import variables


def ranglist_menu():
    print("choices are:\n 1) list by rating \n 2) list by newest\n 3)list most liked in specific genre ")
    choice = input("What do you want to do ", )
    if choice == '1':
        print("Want to list movies by rating")
        rang_liked()
    elif choice == '2':
        print("Want to see the newest movies")
        rang_newest()
    elif choice == '3':
        print("Want to list best rated by genre")
        variables.input_genre()
        rang_genre()
    else:
        variables.wrong_choice()
        ranglist_menu()


def rang_liked():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT MOVIE_NAME, LIKENESS FROM movie ORDER BY LIKENESS DESC LIMIT 5 ;")
    pprint(cur.fetchall())
    conn.commit()


def rang_genre():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    ranged = variables.genre
    cur.execute("SELECT ID,MOVIE_NAME,GENRE,LIKENESS FROM movie WHERE GENRE LIKE ? ORDER BY GENRE DESC LIMIT 5;",
                ['%' + ranged + '%'])
    pprint(cur.fetchall())
    conn.close()


def rang_newest():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT ID,MOVIE_NAME, RELEASE_YEAR FROM movie ORDER BY RELEASE_YEAR DESC LIMIT 5 ;")
    pprint(cur.fetchall())
    conn.commit()
    conn.close()
