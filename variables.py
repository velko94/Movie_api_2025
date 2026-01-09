global movie_name, genre, desc, year, direct, rate


def menu():
    print(
        "(1 want to list all movies \n(2 want to see this movies details \n(3 want to search for a movie "
        "\n(4 want to add a movie"
        "\n(5 Want to add a movie to favorites or see existing favorite\n(6 want to see top 5 movies\n(7 Admin menu")


def wrong_choice():
    print("!!!!!!TRY AGAIN!!!!!")


def name():
    global movie_name
    movie_name = input("what is the name of the movie ")
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
    year = input("what year was it released ")
    try:
        int(year)
    except ValueError:
        wrong_choice()
        release_year()
        return year


def director_name():
    global direct
    direct = input("Who directed the movie ")
    check_input_dir()
    return direct


def user_rating():
    global rate
    rate = float(input("rate the movie "))
    try:
        float(rate)
    except ValueError:
        wrong_choice()
        user_rating()
        return rate


#######################Checks for empty string#######################

def check_input_name():
    if len(movie_name) <= 1:
        wrong_choice()
        name()
    else:
        return movie_name


def check_input_genre():
    if len(genre) <= 1:
        wrong_choice()
        input_genre()
    else:
        return genre


def check_input_desc():
    if len(desc) <= 1:
        wrong_choice()
        description()
    else:
        return desc


def check_input_dir():
    if len(direct) == 0:
        wrong_choice()
        director_name()
    else:
        return direct


# Takes all the required fields and stores them for future use
def user_input():
    name()
    input_genre()
    description()
    director_name()
    release_year()
    user_rating()
    movie_details = (movie_name, genre, direct, desc, year, rate)
    return movie_details
