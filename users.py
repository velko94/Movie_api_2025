import db_connection
import favorites
import variables


def new_user():
    conn, cur = db_connection.get_connection()

    while True:
        user = input("What is your username? ").strip()

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

        favorites.favorites_menu(user)
        break

    conn.close()


def old_user():
    while True:
        username_used = input("what is the username you've registered with? ")

        conn, cur = db_connection.get_connection()
        cur.execute(
            "SELECT USER_NAME FROM users WHERE USER_NAME LIKE ?;",
            [username_used])
        results = cur.fetchone()
        conn.close()

        if results:
            print(f"Greetings {results[0]}")
            favorites.favorites_menu(results[0])
            return results[0]

        else:
            print("No such record!")


def check_user():
    while True:
        user = input("Are you a new user? choices are yes or no ").strip().lower()

        if user == "no":
            return old_user()
        elif user == "yes":
            return new_user()
        else:
            variables.wrong_choice()
            print("Please type yes or no")
