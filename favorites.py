from variables import wrong_choice, check_output
from db_connection import get_connection


def favorites_menu(username):
    print("choices are: \n favlst - list all favorites, \n favadd add movie to favorites,  \n lv - leave menu ")
    favorites_engine(username)


def favorites_engine(username):
    choice = input("What do you want to do ", ).strip().lower()
    if choice == 'favlst':
        print("Soo you want to list favourite movies for the user", username)
        see_list_of_favorites(username)
    elif choice == 'favadd':
        print("Soo you want to add a movie to favourite")
        add_favorite_movie(username)
    elif choice == 'lv':
        print("leave menu")
        import movie_api_GUI
        movie_api_GUI.actions()
    else:
        wrong_choice()
        print("pleaase choose one of the following favlst, favadd, lv")
        favorites_engine(username)


def add_favorite_movie(username):
    ad_fav = input("please type the name of the movie to add: ")
    conn, cur = get_connection()
    cur.execute("SELECT MOVIE_TITLE,GENRE,LIKENESS FROM movie WHERE  MOVIE_TITLE LIKE ?;",
                ["%" + ad_fav + "%"])
    results = cur.fetchall()
    if not results:
        print("No such movie found.")
        conn.close()
        return
    check_output(results)
    favorites_data = [(movie_name, genre, rating, username,) for (movie_name, genre, rating) in results]
    cur.executemany("INSERT INTO favorites (MOVIE_TITLE,GENRE,RATING,FAVORITE_OF) VALUES (?,?,?,?)",
                    favorites_data)
    conn.commit()
    conn.close()
    for movie in results:
        print(f" Movie {movie[0]} was added successfully to favourites for the user {username} ")


def see_list_of_favorites(username):
    conn, cur = get_connection()
    cur.execute(
        "SELECT MOVIE_TITLE, GENRE, RATING FROM favorites WHERE FAVORITE_OF = ?;",
        [username])
    results = cur.fetchall()
    if results:
        from pprint import pprint
        pprint(results)
    else:
        print("No favorites for this user")
    conn.close()
