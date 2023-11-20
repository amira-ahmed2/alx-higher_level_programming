#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print(my_list[i], end="")
                nb_print += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
    return nb_print
