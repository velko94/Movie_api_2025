from movie_list import list_of_movies_admin
import variables
from db_connection import get_connection
from db_actions import recreate_existing_table, table_delete

global movid


def admin_menu():
    print("choice 1:want to list all movies")
    print("choice 2:want to recreate a  table")
    print("choice 3:want to delete a whole table")
    print("choice 4:want to delete a record from a table")
    print("choice 5:want to change something in a record")
    print("choice 6:want to exit the admin menu")


# The functionalities for the admin menu
def admin_actions():
    admin_menu()
    choice = input("What do you want to do use only digits ", )
    if choice == '1':
        list_of_movies_admin()  # called form movie_list
        print("choice 1:want to list all movies")
    elif choice == '2':
        print("Soo choice 2:want to recreate a  table")
        recreate_existing_table()
    elif choice == '3':
        print("choice 3:want to delete a whole table")
        table_delete()
    elif choice == '4':
        print("choice 4: So want to delete a record from a table")
        admin_delete_record()
    elif choice == '5':
        print("choice 5:want to change something in a record")
        admin_update()
    elif choice == '6':
        print("WELCOME THE THE USER MENU")
        from movie_api_GUI import actions
        actions()
    else:
        print("WRONG CHOICE TRY AGAIN")
        admin_menu()


# FUNCTIONS FOR UPDATES ON EXISTING RECORDS#
def check_table():
    conn, cur = get_connection()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cur.fetchall()]
    return tables


def movie_id():
    global movid
    movid = input("What is the id: ")
    if not movid.isdigit():
        print("ID must be a number.")
        return movie_id()
    return int(movid)


def update_name():
    conn, cur = get_connection()
    print("Change the name to the value you wish to be")
    variables.name()
    movie_id()
    cur.execute("UPDATE movie SET MOVIE_TITLE=?WHERE ID=?;", [variables.movie_name, movid])
    conn.commit()
    conn.close()


def update_genre():
    conn, cur = get_connection()
    variables.input_genre()
    movie_id()
    cur.execute("UPDATE movie SET GENRE=?  WHERE ID=? ", [variables.genre, movid])
    conn.commit()
    conn.close()


def update_director():
    conn, cur = get_connection()
    variables.director_name()
    movie_id()
    cur.execute("UPDATE movie SET DIRECTOR=?  WHERE ID=? ", [variables.direct, movid])
    conn.commit()
    conn.close()


def update_desc():
    conn, cur = get_connection()
    variables.description()
    movie_id()
    cur.execute("UPDATE movie SET DESCRIPTION=?  WHERE ID=? ", [variables.description, movid])
    conn.commit()
    conn.close()


def update_year():
    conn, cur = get_connection()
    variables.release_year()
    movie_id()
    cur.execute("UPDATE movie SET RELEASE_YEAR=?  WHERE ID=? ", [variables.year, movid])
    conn.commit()
    conn.close()


# to update a single record in the db uses above functions
def admin_update():
    print("choices are 'name', 'genre', 'director', 'description', 'year' ")
    update = input("what to update ")
    if update == 'name':
        update_name()
    elif update == 'description':
        update_desc()
    elif update == 'year':
        update_year()
    elif update == 'director':
        update_director()
    elif update == 'genre':
        update_genre()
    else:
        print("Wrong choice")


# Deleting just a record from the table
def admin_delete_record():
    allowed_tables = check_table()
    table_to_delete = input("What is the name of the table: ")
    if table_to_delete not in allowed_tables:
        print("Invalid table name!")
        return admin_delete_record()
    movies_id = movie_id()
    conn, cur = get_connection()
    cur.execute(f"SELECT 1 FROM {table_to_delete} WHERE ID = ?", (movies_id,))
    result = cur.fetchone()
    if not result:
        print(f"No record with ID {movies_id} in table {table_to_delete}.")
        conn.close()
        return admin_delete_record()
    else:
        conn, cur = get_connection()  # called from db_connections
        cur.execute(f"DELETE FROM {table_to_delete} WHERE ID = ?;", (movies_id,))

        print("record", movies_id, "was deleted  from", table_to_delete)
        # To reset the id's and keep them in correct order
        cur.execute("DELETE FROM sqlite_sequence WHERE name='movie'")
        conn.commit()
        conn.close()
