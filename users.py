from favorites import favorites_menu
from variables import wrong_choice
from db_connection import get_connection
global record, username


def new_user():
    conn, cur = get_connection()

    while True:
        user = input("What is your username? ")
        if len(user) <= 3:
            print("Must be at least 4 characters long")
            continue

        # check if username already exists
        cur.execute("SELECT USER_NAME FROM users WHERE USER_NAME = ?", [user])
        if cur.fetchone():
            print("This username already exists. Choose a different one.")
            continue

        # insert new user
        cur.execute("INSERT INTO Users (USER_NAME) VALUES (?)", [user])
        conn.commit()
        print(f"The user {user} was added to table users")
        print("Greetings", user.upper())
        favorites_menu(user)
        break

    conn.close()


def old_user():
    username_used = input("what is the username you've registered with? ")
    conn, cur = get_connection()
    cur.execute(
        "SELECT USER_NAME FROM users WHERE USER_NAME LIKE ?;",
        [username_used])
    results = cur.fetchone()
    if results:
        print(f"Greetings {results[0]}")
        favorites_menu(results[0])
        return results[0]
    else:
        print("No such record!")
        old_user()


def check_user():
    user = input("Are you a new user? choices are yes or no ").strip().lower()
    answer1 = "no"
    answer2 = "yes"
    if user == answer1:
        old_user()
    elif user == answer2:
        new_user()
    else:
        wrong_choice()
        check_user()
