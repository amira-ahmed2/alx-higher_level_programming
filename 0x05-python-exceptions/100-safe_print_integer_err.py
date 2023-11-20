#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as v_error:
        import sys
        print("Exception: {}".format(v_error), file=sys.stderr)
        return False
