#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        import sys
        print("Exception: Could not print the value as an integer", file=sys.stderr)
        return False
    else:
        return True

