import sys
from movie_add import adding
from movie_search import search_menu
from movie_details import details
from movie_ranglist import ranglist_menu
from movie_list import list_of_movies
from admin_options import admin_actions
import variables
from users import check_user


def actions(choice=None):
    if choice is None:
        variables.menu()
        choice = input("What do you want to do ", ).strip().lower()
    else:
        choice = choice.lower()
    if choice in ['movlst', '--movlst']:
        print("Listing all movies")
        list_of_movies()
        all_done()
    elif choice in ['movdt', '--movdt']:
        print("Showing movies details")
        details()
        all_done()
    elif choice in ['movsrch', '--movsrch']:
        print("Searching for a movie")
        search_menu()
        all_done()
    elif choice in ['movadd', '--movadd']:
        print("Adding a movie")
        adding()
        all_done()
    elif choice in ['movfv', '--movfv']:
        print("Opening favorites!")
        # from users call check user variable\
        check_user()
        all_done()
    elif choice in ['movcat', '--movcat']:
        print("Showing top 5 movies")
        ranglist_menu()  # from movie_ranglist
        all_done()
    elif choice in ['movadm', '--movadm']:
        print("Showing ADMIN MENU")
        admin_actions()
        all_done()
    elif choice == "exit":
        print("Alright, have a nice day!")
        sys.exit(0)
    else:
        variables.wrong_choice()
        if choice.startswith('--'):
            sys.exit(1)
        else:
            actions()


# asking the person if he wants to continue

def all_done():
    done = input("Want to do something more? ").strip().lower()
    if done == 'no':
        print("Alright have a nice day")
        sys.exit(0)
    elif done == 'yes':
        actions()
    else:
        variables.wrong_choice()
        print("Ivalid choice please type yes or no")
        all_done()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Take the first CLI argument as the choice
        actions(sys.argv[1])
    else:
        actions()
