import variables
import db_actions
import db_connection
import movie_list


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
    while True:
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
            return
        else:
            print("WRONG CHOICE TRY AGAIN")


def run_update(query, params):
    conn, cur = db_connection.get_connection()
    try:
        cur.execute(query, params)
        conn.commit()
    finally:
        conn.close()


# FUNCTIONS FOR UPDATES ON EXISTING RECORDS#

def movie_id():
    while True:
        movid = input("What is the id: ").strip()
        if movid.isdigit():
            return int(movid)

        print("ID must be a number.")


def update_name():
    print("Change the name to the value you wish to be")
    new_name = variables.name()
    id_value = movie_id()
    run_update("UPDATE movie SET MOVIE_TITLE=? WHERE ID=?;", [new_name, id_value])


def update_genre():
    new_genre = variables.input_genre()
    id_value = movie_id()
    run_update("UPDATE movie SET GENRE=?  WHERE ID=? ", [new_genre, id_value])


def update_director():
    new_dir = variables.director_name()
    id_value = movie_id()
    run_update("UPDATE movie SET DIRECTOR=?  WHERE ID=? ", [new_dir, id_value])


def update_desc():
    new_desc = variables.description()
    id_value = movie_id()
    run_update("UPDATE movie SET DESCRIPTION=?  WHERE ID=? ", [new_desc, id_value])


def update_year():
    new_year = variables.release_year()
    id_value = movie_id()
    run_update("UPDATE movie SET RELEASE_YEAR=?  WHERE ID=? ", [new_year, id_value])


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
    while True:
        allowed_tables = [t.lower() for t in db_actions.check_existing_tables()]
        table_to_delete = input("What is the name of the table: ").strip().lower()
        if table_to_delete not in allowed_tables:
            print("Invalid table name!")
            continue

        movies_id = movie_id()
        conn, cur = db_connection.get_connection()
        cur.execute(f"SELECT 1 FROM {table_to_delete} WHERE ID = ?", (movies_id,))
        result = cur.fetchone()

        if not result:
            print(f"No record with ID {movies_id} in table {table_to_delete}.")
            conn.close()
            continue

        cur.execute(f"DELETE FROM {table_to_delete} WHERE ID = ?;", (movies_id,))
        conn.commit()
        conn.close()
        print("record", movies_id, "was deleted  from", table_to_delete)
        return
