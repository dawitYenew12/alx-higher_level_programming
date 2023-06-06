#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) not in range(65, 91):
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end="")
    print()
