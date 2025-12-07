# TABLE MANAGEMENT FUNCTIONS#
from pprint import pprint

import variables
from db_connection import get_connection


# creating the movie table
def movie_table():
    conn, cur = get_connection()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS movie (
    ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    MOVIE_TITLE TEXT NOT NULL UNIQUE,
    GENRE TEXT,
    DIRECTOR TEXT,
    DESCRIPTION TEXT,
    RELEASE_YEAR INTEGER,
    LIKENESS INTEGER);'''
    )
    conn.commit()
    conn.close()


# creating the users table
def users_table():
    conn, cur = get_connection()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_NAME TEXT NOT NULL UNIQUE);'''
                )
    conn.commit()
    conn.close()


# create the favourites table
def favorites_table():
    conn, cur = get_connection()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS favorites (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_TITLE TEXT NOT NULL,
        GENRE TEXT,
        RATING FLOAT,
        FAVORITE_OF TEXT,
        FOREIGN KEY (FAVORITE_OF) REFERENCES users(USER_NAME),
        FOREIGN KEY (MOVIE_TITLE) REFERENCES movie(MOVIE_TITLE)
    );'''
    )
    conn.commit()
    conn.close()


# deleting a table

def table_delete():
    while True:

        table = str(input("what is the name of the table you want to drop "))
        existing_tables = check_existing_tables()
        if table == "":
            print("Table name can't be empty")
            continue

        if table not in existing_tables:
            print(f"Table '{table}' does not exist.")
            return

        conn, cur = get_connection()
        cur.execute(f"DROP TABLE {table};")
        conn.commit()
        conn.close()
        print(f"Table {table} was deleted.")
        return


# fallback if you delete the wrong table
def recreate_existing_table():
    while True:
        table_name = input("What is the name of the table ").strip().lower()
        existing = [t.lower() for t in check_existing_tables()]

        if table_name in existing:
            print(f"Table '{table_name}' already exists.")
            return "exists"

        if table_name == 'movie':
            movie_table()
            print("table movie was created")
            return
        elif table_name == 'favorites':
            favorites_table()
            print("table favorites was created")
            return
        elif table_name == 'users':
            users_table()
            print("table users was created")
            return
        variables.wrong_choice()


# Major check if the tabel exists
def get_unique_movie_title(exclude_id=None):
    title = variables.name()

    conn, cur = get_connection()

    if exclude_id is not None:
        cur.execute(
            "SELECT 1 FROM movie WHERE MOVIE_TITLE=? AND ID!=?", (title, exclude_id)
        )
    else:
        cur.execute(
            "SELECT 1 FROM movie WHERE MOVIE_TITLE=?", (title,)
        )

    exists = cur.fetchone()
    conn.close()

    if exists:
        print(f"'{title}' already exists. Please enter a different title.")
        return get_unique_movie_title(exclude_id)

    return title


def check_existing_tables():
    conn, cur = get_connection()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )
    table_exist = [row[0] for row in cur.fetchall()]
    conn.close()
    print(f"Table {table_exist} already exists in the db ")
    return table_exist


# if the tables are not quite good, or you have some issue with the keys or column names
# should be called specifically no option of it yet
def check_db_state():
    conn, cur = get_connection()
    cur.execute(
        "PRAGMA table_info(movie);"
    )

    pprint(cur.fetchall())
    conn.close()


def list_tables():
    conn, cur = get_connection()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )
    tables = [row[0] for row in cur.fetchall()]
    conn.close()
    print(tables)
    return tables


# The bellow should be used if the table must be altered or was created wrong
def copy_existing_table():
    conn, cur = get_connection()
    cur.execute(
        '''CREATE TABLE movie_new (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MOVIE_TITLE TEXT NOT NULL UNIQUE,
    GENRE TEXT,
    DIRECTOR TEXT,
    DESCRIPTION TEXT,
    RELEASE_YEAR INTEGER,
    LIKENESS INTEGER
);'''
    )
    conn.commit()
    conn.close()


# Copies the current data of the table
def actual_copy():
    conn, cur = get_connection()
    cur.execute(
        '''INSERT INTO movie_new (ID, MOVIE_TITLE, GENRE, DIRECTOR, DESCRIPTION, RELEASE_YEAR, LIKENESS)
  SELECT ID, MOVIE_TITLE, GENRE, DIRECTOR, DESCRIPTION, RELEASE_YEAR, LIKENESS
  FROM movie;'''
    )
    conn.commit()
    conn.close()


# This should be used after the table was correctly recreated
def change_name_of_table():
    conn, cur = get_connection()
    cur.execute(
        'ALTER TABLE movie_new RENAME TO movie;'
    )
    conn.commit()
    conn.close()
