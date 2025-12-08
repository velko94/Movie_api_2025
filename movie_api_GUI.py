import sys
import os

import admin_options
import movie_add
import movie_details
import movie_list
import movie_ranglist
import movie_search
import users
import variables

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def actions(choice=None):
    while True:

        if choice is None:
            variables.menu()
            choice = input("What do you want to do ", ).strip().lower()
        else:
            choice = choice.lower()

        if choice in ['movlst', '--movlst']:
            print("Listing all movies")
            movie_list.list_of_movies()

        elif choice in ['movdt', '--movdt']:
            print("Showing movies details")
            movie_details.details()

        elif choice in ['movsrch', '--movsrch']:
            print("Searching for a movie")
            movie_search.search_menu()

        elif choice in ['movadd', '--movadd']:
            print("Adding a movie")
            movie_add.adding()

        elif choice in ['movfv', '--movfv']:
            print("Opening favorites!")
            # from users call check user variable\
            users.check_user()

        elif choice in ['movcat', '--movcat']:
            print("Showing top 5 movies")
            movie_ranglist.ranglist_menu()  # from movie_ranglist

        elif choice in ['movadm', '--movadm']:
            print("Showing ADMIN MENU")
            admin_options.admin_menu()

        elif choice == "exit":
            print("Alright, have a nice day!")
            sys.exit(0)
        else:
            variables.wrong_choice()
            choice = None
            continue
        if not all_done():
            sys.exit(0)
        clear_screen()
        choice = None

# asking the person if he wants to continue

def all_done():
    while True:
        done = input("Want to do something more? ").strip().lower()

        if done == 'yes':
            return True

        if done == 'no':
            print("Alright have a nice day")
            return False

        variables.wrong_choice()
        print("Invalid choice please type yes or no")


# Used so that the main command can be called from the terminal directly
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Take the first CLI argument as the choice
        actions(sys.argv[1])
    else:
        actions()

