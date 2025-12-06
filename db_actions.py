# TABLE MANAGEMENT FUNCTIONS#
from db_connection import get_connection
global exists
from variables import wrong_choice
from pprint import pprint

# creating the movie table
def movie_table():
    conn = get_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS movie (
    ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    MOVIE_TITLE TEXT NOT NULL UNIQUE,
    GENRE TEXT,
    DIRECTOR TEXT,
    DESCRIPTION TEXT,
    RELEASE_YEAR INTEGER,
    LIKENESS INTEGER);''')
    conn.commit()
    conn.close()


# creating the users table
def users_table():
    conn, cur = get_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_NAME TEXT NOT NULL UNIQUE);''')
    conn.commit()
    conn.close()


# create the favourites table
def favorites_table():
    conn, cur = get_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS favorites (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_TITLE TEXT NOT NULL,
        GENRE TEXT,
        RATING FLOAT,
        FAVORITE_OF TEXT,
        FOREIGN KEY (FAVORITE_OF) REFERENCES users(USER_NAME),
        FOREIGN KEY (MOVIE_TITLE) REFERENCES movie(MOVIE_TITLE)
    );''')
    conn.commit()
    conn.close()


# deleting a table

def table_delete():
    conn, cur = get_connection()
    table = str(input("what is the name of the table you want to drop "))
    existing_tables = check_existing_tables()
    if table == "":
        print("Table name can't be empty")
    elif table not in existing_tables:
        print(f"Table '{table}' does not exist.")
        conn.close()
        table_delete()
    else:
        cur.execute(f"DROP TABLE {table};")
        print(f"Table '{table}' was deleted.")
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
        print("table movie was created")
    elif table_name == choice2:
        favorites_table()
        print("table favorites was created")
    elif table_name == choice3:
        users_table()
        print("table users was created")
    else:
        wrong_choice()
        recreate_existing_table()


def check_existing_tables():
    conn, cur = get_connection()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_exist = [row[0] for row in cur.fetchall()]
    conn.close()
    return table_exist


# if the tables are not quite good, or you have some issue with the keys or column names
def check_db_state():
    conn, cur = get_connection()
    cur.execute("PRAGMA table_info(movie);")

    pprint(cur.fetchall())
    conn.close()


def list_tables():
    conn, cur = get_connection()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cur.fetchall()]
    conn.close()
    print(tables)
    return tables


# fixing the table movie without losing the data
def copy_existing_table():
    conn, cur = get_connection()
    cur.execute('''CREATE TABLE movie_new (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MOVIE_TITLE TEXT NOT NULL UNIQUE,
    GENRE TEXT,
    DIRECTOR TEXT,
    DESCRIPTION TEXT,
    RELEASE_YEAR INTEGER,
    LIKENESS INTEGER
);''')
    conn.commit()
    conn.close()


def actual_copy():
    conn, cur = get_connection()
    cur.execute('''INSERT INTO movie_new (ID, MOVIE_TITLE, GENRE, DIRECTOR, DESCRIPTION, RELEASE_YEAR, LIKENESS)
  SELECT ID, MOVIE_TITLE, GENRE, DIRECTOR, DESCRIPTION, RELEASE_YEAR, LIKENESS
  FROM movie;''')
    conn.commit()
    conn.close()


def change_name_of_table():
    conn, cur = get_connection()
    conn.execute('ALTER TABLE movie_new RENAME TO movie;')
    conn.commit()
    conn.close()


def get_unique_movie_title(exclude_id=None):
    global exists
    conn, cur = get_connection()
    from variables import name
    title = name()
    if exclude_id:
        cur.execute("SELECT 1 FROM movie WHERE MOVIE_TITLE=? AND ID!=?", (title, exclude_id))
    else:
        cur.execute("SELECT 1 FROM movie WHERE MOVIE_TITLE=?", (title,))
        exists = cur.fetchone()
    if exists:
        print(f"'{title}' already exists. Please enter a different title.")
        conn.close()
        return get_unique_movie_title(exclude_id)
    else:
        conn.close()
        return title
