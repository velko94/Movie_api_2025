import movie_add, movie_search, movie_details, movie_ranglist, movie_list, admin_options
import variables


def actions():
    # to print out the menu
    from variables import menu
    menu()
    choice = input("What do you want to do ", )
    if choice == '1':
        print("SOO you want to list all movies")
        movie_list.list_of_movies()
        all_done()

    elif choice == '2':
        print("SOO you want to see this movies details")
        movie_details.details()
        all_done()
    elif choice == '3':
        print("SOO you want to search for a movie")
        movie_search.search_engine()
        all_done()
    elif choice == '4':
        print("SOO you want to add a movie")
        movie_add.adding()
        all_done()
    elif choice == '5':
        from users import check_user
        print("You chosen favorite!")
        # from users call check user variable\
        check_user()
        all_done()
    elif choice == '6':
        print("SOO you want to see top 5 movies")
        movie_ranglist.ranglist_menu()
        all_done()
    elif choice == '7':
        print("SOO you want to open admin menu")
        admin_options.admin_actions()
        all_done()
    else:
        variables.wrong_choice()
        actions()


# asking the person if he wants to continue

def all_done():
    done = str(input("Want to do something more? "))
    if done == 'no':
        print("Alright have a nice day")
    elif done == 'yes':
        actions()
    else:
        variables.wrong_choice()
        all_done()


actions()
