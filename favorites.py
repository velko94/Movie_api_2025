from pprint import pprint
import db_connection
import variables


def favorites_menu(username):
    print("choices are: \n favlst - list all favorites, \n favadd add movie to favorites,  \n lv - leave menu ")
    favorites_engine(username)


def favorites_engine(username):
    while True:
        choice = input("What do you want to do in the favorites menu ", ).strip().lower()

        if choice == 'favlst':
            print("Soo you want to list favourite movies for the user", username)
            see_list_of_favorites(username)

        elif choice == 'favadd':
            print("Soo you want to add a movie to favourite")
            add_favorite_movie(username)

        elif choice == 'lv':
            print("leave menu")
            from movie_api_GUI import actions
            actions()
            return

        else:
            variables.wrong_choice()
            print("please choose one of the following favlst, favadd, lv")


def add_favorite_movie(username):
    ad_fav = input("please type the name of the movie to add: ").strip(

    )
    conn, cur = db_connection.get_connection()
    cur.execute("SELECT MOVIE_TITLE,GENRE,LIKENESS FROM movie WHERE  MOVIE_TITLE LIKE ?;",
                ["%" + ad_fav + "%"])

    results = cur.fetchall()

    if not results:
        print("No such movie found.")
        conn.close()
        return

    for (movie_name, genre, rating) in results:

        if check_existing_favorite(username, movie_name):
            print(f"Movie '{movie_name}' is already in favorites for user '{username}'.")
            continue

        else:
            favorites_data = (movie_name, genre, rating, username,)
            cur.execute("INSERT INTO favorites (MOVIE_TITLE,GENRE,RATING,FAVORITE_OF) VALUES (?,?,?,?)",
                        favorites_data)

            print(f" Movie {favorites_data[0]} was added successfully to favourites for the user {username} ")
    conn.commit()
    conn.close()


def see_list_of_favorites(username):
    conn, cur = db_connection.get_connection()
    cur.execute(
        "SELECT MOVIE_TITLE, GENRE, RATING FROM favorites WHERE FAVORITE_OF = ?;", [username]
    )
    results = cur.fetchall()
    if results:
        pprint(results)
    else:
        print("No favorites for this user")
    conn.close()


def check_existing_favorite(username, movie_title):
    conn, cur = db_connection.get_connection()
    cur.execute("""
        SELECT 1 
        FROM favorites 
        WHERE MOVIE_TITLE = ? AND FAVORITE_OF = ?;
    """, (movie_title, username))

    results = cur.fetchone()
    conn.close()
    return results is not None
