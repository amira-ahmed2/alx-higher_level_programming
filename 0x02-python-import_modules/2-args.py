#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1

    if number == 1:
        print("{} arguments.".format(number))
    elif number == 0:
        print("{} argument:".format(number))
    else:
        print("{} argument:".format(number))

    if number >= 1:
        number = 0
        for i in sys.argv:
            if number != 0:
                print("{}: {}".format(number, i))
            number += 1
