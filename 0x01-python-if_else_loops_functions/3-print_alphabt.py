#!/usr/bin/python3
for num in range(97, 123):
    if num not in {101, 113}:
        print("{}".format(chr(num)), end="")
