from pprint import pprint

import db_actions

global movie_name, genre, desc, year, direct, rate


def menu():
    print(
        " movslt - want to list all movies "
        "\n movdt - want to see this movies details  "
        "\n movsrch - want to search for a movie"
        "\n movadd - want to add a movie "
        "\n movfv - Want to add a movie to favorites or see existing favorite "
        " \n movcat - want to see top 5 movies "
        " \n movadm - Admin menu "
        " \n exit - exit the menu")


def wrong_choice():
    print("TRY AGAIN!")


def name():
    global movie_name
    movie_name = input("what is the name of the movie ").strip().lower()
    check_input_name()
    return movie_name


def input_genre():
    global genre
    genre = input("In what genre is the movie ")
    check_input_genre()
    return genre


def description():
    global desc
    desc = input("Please say something about the movie ")
    check_input_desc()
    return desc


def release_year():
    global year
    while True:
        year = input("Which year was it released? ")
        if year.isdigit() and len(year) >= 3:
            return int(year)
        print("Please type a correct year (digits only, at least 3 characters).")


def director_name():
    global direct
    direct = input("Who directed the movie ")
    check_input_dir()
    return direct


def user_rating():
    global rate
    rate = input("rate the movie ")
    try:
        rate = float(rate)
        return rate
    except ValueError:
        wrong_choice()
        print("Invalid input. Please enter a correct number. (e.g. 3.5)")
        return user_rating()


# Checks for the user input#

def check_input_name():
    if len(movie_name) <= 1:
        wrong_choice()
        print("Not a correct name")
        return name()
    return movie_name


def check_input_genre():
    if len(genre) <= 1:
        wrong_choice()
        print("Not a correct genre")
        return input_genre()
    return genre


def check_input_desc():
    if len(desc) <= 1:
        wrong_choice()
        print("Not a correct description")
        return description()
    return desc


def check_input_dir():
    if len(direct) == 0:
        wrong_choice()
        print("Not a correct director")
        return director_name()
    return direct


# Takes all the required fields and stores them for future use
def user_input():
    global movie_name
    movie_name = db_actions.get_unique_movie_title()
    description()
    release_year()
    director_name()
    input_genre()
    user_rating()
    movie_details = (movie_name, desc, year, direct, genre, rate)
    return movie_details


def check_output(results):
    if results and len(results) > 0:
        pprint(results)
    else:
        print("No such record!")
