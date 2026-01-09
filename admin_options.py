import movie_list
import variables, db_actions
global movid


def admin_menu():
    print("choice 1:want to list all movies")
    print("choice 2:want to recreate a  table")
    print("choice 3:want to delete a whole table")
    print("choice 4:want to delete a record from a table")
    print("choice 5:want to change something in a record")
    print("choice 6:want to exit the admin menu")


def admin_actions():
    admin_menu()
    choice = input("What do you want to do ", )
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
        print("Wrong choice")
        admin_menu()


####################################### FUNCTIONS FOR UPDATES ON EXISTING RECORDS######################################
def movie_id():
    global movid
    movid = input("What is the id of the movie ")
    return movid


def update_name():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    variables.name()
    movie_id()
    cur.execute("UPDATE movie SET MOVIE_NAME=?WHERE ID=?;", [variables.movie_name, movid])
    conn.commit()
    conn.close()


def update_genre():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    variables.input_genre()
    movie_id()
    cur.execute("UPDATE movie SET GENRE=?  WHERE ID=? ", [variables.genre, movid])
    conn.commit()
    conn.close()


def update_director():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    variables.director_name()
    movie_id()
    cur.execute("UPDATE movie SET DIRECTOR=?  WHERE ID=? ", [variables.direct, movid])
    conn.commit()
    conn.close()


def update_desc():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    variables.description()
    movie_id()
    cur.execute("UPDATE movie SET DESCRIPTION=?  WHERE ID=? ", [variables.description, movid])
    conn.commit()
    conn.close()


def update_year():
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    variables.release_year()
    movie_id()
    cur.execute("UPDATE movie SET RELEASE_YEAR=?  WHERE ID=? ", [variables.year, movid])
    conn.commit()
    conn.close()


def admin_update():
    update = str(input("what to update "))
    update_choice = ['name', 'genre', 'director', 'description', 'year']
    if update == update_choice[0]:
        update_name()
    elif update == update_choice[1]:
        update_genre()
    elif update == update_choice[2]:
        update_director()
    elif update == update_choice[3]:
        update_desc()
    elif update == update_choice[4]:
        update_year()
    else:
        print("Wrong choice")


# NOT working for the moment
# def update_id():
#     name()
#     movie_id()
#     cur.execute("UPDATE movie SET ID=?  WHERE MOVIE_NAME=? ", [movid,movie_name])
#     conn.commit()

#Deleting just a record from the table
def admin_delete_record():
    table_to_delete = input("what is the name of the table ")
    movie_id()
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table_to_delete} WHERE ID = ? ;", [movid])
    # db_actions.check_existing_tables()
    conn.commit()
    conn.close()
    print("record", movid, "was deleted  from", table_to_delete)
