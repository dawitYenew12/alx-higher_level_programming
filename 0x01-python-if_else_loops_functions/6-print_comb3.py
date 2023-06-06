#!/usr/bin/python3
for d1 in range(9):
    for d2 in range(d1 + 1, 10):
        #if it is the last
        if d1 == 8 and d2 == 9:
            print("{:d}{:d}".format(d1, d2))
        else:
            print("{:d}{:d}".format(d1, d2), end=", ")
