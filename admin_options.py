import variables
import db_actions
import db_connection
import movie_list

global movid


def admin_menu():
    print("choice 1:want to list all movies")
    print("choice 2:want to recreate a  table")
    print("choice 3:want to delete a whole table")
    print("choice 4:want to delete a record from a table")
    print("choice 5:want to change something in a record")
    print("choice 6:want to exit the admin menu")
    admin_actions()


# The functionalities for the admin menu
def admin_actions():

    choice = input("What do you want to do use only digits ", )
    if choice == '1':
        movie_list.list_of_movies_admin()
        print("choice 1:want to list all movies")
    elif choice == '2':
        print("Soo choice 2:want to recreate a  table")
        db_actions.recreate_existing_table()
    elif choice == '3':
        print("choice 3:want to delete a whole table")
        db_actions.table_delete()
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


def run_update(query, params):
    conn, cur = db_actions.get_connection()
    try:
        cur.execute(query, params)
        conn.commit()
    finally:
        conn.close()


# FUNCTIONS FOR UPDATES ON EXISTING RECORDS#

def movie_id():
    global movid
    movid = input("What is the id: ")
    if not movid.isdigit():
        print("ID must be a number.")
        return movie_id()
    return int(movid)


def update_name():
    print("Change the name to the value you wish to be")
    variables.name()
    movie_id()
    run_update("UPDATE movie SET MOVIE_TITLE=? WHERE ID=?;", [variables.movie_name, movid])


def update_genre():
    variables.input_genre()
    movie_id()
    run_update("UPDATE movie SET GENRE=?  WHERE ID=? ", [variables.genre, movid])


def update_director():
    variables.director_name()
    movie_id()
    run_update("UPDATE movie SET DIRECTOR=?  WHERE ID=? ", [variables.direct, movid])


def update_desc():
    variables.description()
    movie_id()
    run_update("UPDATE movie SET DESCRIPTION=?  WHERE ID=? ", [variables.description, movid])


def update_year():
    variables.release_year()
    movie_id()
    run_update("UPDATE movie SET RELEASE_YEAR=?  WHERE ID=? ", [variables.year, movid])


# THis is the engine for updating a single record in the db and uses above functions
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
    allowed_tables = db_actions.check_existing_tables()
    table_to_delete = input("What is the name of the table: ")
    if table_to_delete not in allowed_tables:
        print("Invalid table name!")
        return admin_delete_record()
    movies_id = movie_id()
    conn, cur = db_connection.get_connection()
    cur.execute(f"SELECT 1 FROM {table_to_delete} WHERE ID = ?", (movies_id,))
    result = cur.fetchone()
    if not result:
        print(f"No record with ID {movies_id} in table {table_to_delete}.")
        conn.close()
        return admin_delete_record()
    else:
        cur.execute(f"DELETE FROM {table_to_delete} WHERE ID = ?;", (movies_id,))
        print("record", movies_id, "was deleted  from", table_to_delete)
        # To reset the id's and keep them in correct order
        cur.execute("DELETE FROM sqlite_sequence WHERE name='movie'")
        conn.commit()
        conn.close()
