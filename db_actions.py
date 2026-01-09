############ TABLE MANAGEMENT FUNCTIONS###############################
import variables


def table_delete():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    table = str(input("what is the name of the table you want to drop "))
    if table != "":
        cur.execute(f"DROP TABLE {table};")
        conn.commit()
        conn.close()
    else:
        print("cant be empty")


# creating the users table
def users_table():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY,USER_NAME VARCHAR (15))")
    conn.commit()
    conn.close()


# creating the movie table
def movie_table():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS movie (
     ID INTEGER PRIMARY KEY,
     MOVIE_NAME VARCHAR (70),
     GENRE STRING (30),
     DIRECTOR STRING(20),
     DESCRIPTION VARCHAR (850),
     RELEASE_YEAR INTEGER (4),LIKENESS INTEGER (2))''')
    conn.commit()
    conn.close()


def favorites_table():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS Favorites (
            ID INTEGER PRIMARY KEY,
            MOVIE_NAME VARCHAR (70),
            GENRE STRING (30),
            RATING FLOAT (3),
            FAVORITE_OF STRING (20))
            ''')
    conn.commit()
    conn.close()


def users_table():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY,
            USER_NAME VARCHAR (20))
            ''')
    conn.commit()
    conn.close()

# failback if you delete the wrong table


def recreate_existing_table():
    table_name = input("What is the name of the table ")
    choice1 = 'movie'
    choice2 = 'favorites'
    choice3 = 'users'
    if table_name == choice1:
        movie_table()
    elif table_name == choice2:
        favorites_table()
    elif table_name == choice3:
        users_table()
    else:
        variables.wrong_choice()
        recreate_existing_table()


def check_existing_tables():
    import sqlite3
    conn = sqlite3.connect('Movie.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_exist = [cur.fetchone()]
    conn.commit()
    conn.close()
    if table_exist:
        print("no such table")
    elif table_exist:
        print(table_exist)
    else:
        print('table was deleted')
