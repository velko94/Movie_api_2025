from pprint import pprint

import db_actions


def menu():
    print(
        " movlst - want to list all movies "
        "\n movdt - want to see this movies details  "
        "\n movsrch - want to search for a movie"
        "\n movadd - want to add a movie "
        "\n movfv - Want to add a movie to favorites or see existing favorite "
        " \n movcat - want to see top 5 movies "
        " \n movadm - Admin menu "
        " \n exit - exit the menu")

# global helper moslty used for debug purpose
def wrong_choice():
    print("TRY AGAIN!")

# Global helper to take the data from the customer
def name():
    while True:
        movie_name = input("what is the name of the movie ").strip()

        if len(movie_name) > 1:
            return movie_name

        wrong_choice()
        print("Not a correct name")


def input_genre():
    while True:
        genre = input("In what genre is the movie ").strip()

        if len(genre) > 1:
            return genre

        wrong_choice()
        print("Not a correct genre")


def description():
    while True:
        desc = input("Please say something about the movie ").strip()

        if len(desc) > 1:
            return desc

        wrong_choice()
        print("Not a correct description")


def release_year():
    while True:
        year = input("Which year was it released? ").strip()

        if year.isdigit() and len(year) >= 3:
            return int(year)

        wrong_choice()
        print("Please type a correct year (digits only, at least 3 characters).")


def director_name():
    while True:
        direct = input("Who directed the movie ").strip()
        if len(direct) > 1:
            return direct
        wrong_choice()
        print("Not a correct director")


def user_rating():
    while True:
        rate = input("rate the movie ")

        try:
            return float(rate)

        except ValueError:
            wrong_choice()
            print("Invalid input. Please enter a correct number. (e.g. 3.5)")


# Takes all the required fields and stores them for future use
def user_input():
    movie_name = db_actions.get_unique_movie_title()
    desc = description()
    year = release_year()
    direct = director_name()
    genre = input_genre()
    rate = user_rating()
    return (movie_name, desc, year, direct, genre, rate)


# Global helper to print if the sql query comes empty
def check_output(results):
    if results and len(results) > 0:
        pprint(results)
    else:
        print("No such record!")
