#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal's triangle
"""


def pascal_triangle(n):
    """A function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal's triangle of n"""
    ans = []
    if n <= 0:
        return ans

    for i in range(n):
        row = []
        C = 1
        for j in range(i + 1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        ans.append(row)

    return ans
