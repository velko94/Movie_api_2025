import favorites
import variables


def new_username():
    global username
    username = input("what is your username? ")
    if len(username) <= 2:
        variables.wrong_choice()
        print("Must be at least 4 chars")
        new_username()
    else:
        import sqlite3
        conn = sqlite3.connect("Movie.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Users (USER_NAME) VALUES(?)", [username])
        conn.commit()
        conn.close()
    print("Welcome", username)
    favorites.favorites_menu()


def old_user():
    username = input("what is the username you've registered with? ")
    import sqlite3
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT USER_NAME FROM users WHERE USER_NAME LIKE ?;",
        [username])
    global record
    record = cur.fetchone()
    conn.close
    if record is None:
        print("no such user")
        check_user()
    else:
        print("Welcome", record)
        favorites.favorites_menu()


def check_user():
    user = input("Are you a new user? ")
    answer1 = "no"
    answer2 = "yes"
    if user == answer1:
        old_user()
    elif user == answer2:
        new_username()
    else:
        variables.wrong_choice()
        check_user()
