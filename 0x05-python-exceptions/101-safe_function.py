#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except ZeroDivisionError as zero_err:
        print("Exception: " + zero_err.args[0], file=sys.stderr)
        return None
    except IndexError as ind_err:
        print("Exception: " + ind_err.args[0], file=sys.stderr)
        return None
