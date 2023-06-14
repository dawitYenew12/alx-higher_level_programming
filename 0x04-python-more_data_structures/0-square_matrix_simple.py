#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for num in matrix:
        copy.append(list(map(lambda num: num**2, num)))
    return (copy)
