from pprint import pprint
import variables


def favorites_menu():
    print("choices are: 1) list all favorites 2) add movie to favorites  3)leave menu ")
    choice = input("What do you want to do ", )
    if choice == '1':
        print("Soo you want to list favourite movies")
        see_list_of_favorites()
    elif choice == '2':
        print("Soo you want to add a movie to favourite")
        add_favorite_movie()
    elif choice == '3':
        print("leave menu")
        import movie_api_GUI
        movie_api_GUI.actions()
    else:
        variables.wrong_choice()
        favorites_menu()


def add_favorite_movie():
    ad_fav = input("please type the name of the movie to add ")
    # user_fav = input("for which user to add it ")
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT MOVIE_NAME,GENRE,LIKENESS FROM movie WHERE  MOVIE_NAME LIKE ?;",
                [ad_fav])
    output = cur.fetchall()
    if output == []:
        print("No such movie")
        favorites_menu()
    else:
        cur.executemany("INSERT INTO Favorites(MOVIE_NAME,GENRE,RATING) VALUES (?,?,?)",
                        output)
        conn.commit()
        conn.close()
    print("The movie", output, "was added successfully")


def see_list_of_favorites():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Favorites;")
    pprint(cur.fetchall())
    conn.close()
