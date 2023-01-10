#!/usr/bin/python3
'''
pascal_triangle function
'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing the
    Pascal's triangle of n
    '''
    if n <= 0:
        return []
    pascal = [[] for i in range(n)]
    i = 0
    while i < n:
        if i == 0:
            pascal[0] = [1]
        elif i == 1:
            pascal = [1, 1]
        else:
            pascal[i].append(1)
            for x in range(len(pascal[i - 1]) - 1):
                a = pascal[i - 1][x:x + 2]
                pascal[i].append(sum(a))
            pascal[i].append(1)
        i += 1
    return pascal
