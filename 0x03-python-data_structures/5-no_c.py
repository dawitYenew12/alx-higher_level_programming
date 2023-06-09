#!/usr/bin/python3
def no_c(my_string):
    list_copy = [ch for ch in my_string if ch not in {"c", "C"}]
    return ("".join(list_copy))
