#!/usr/bin/python3
"""
 Calculates the fewest number of operations needed
"""
import math


def lar_div(n):
    """
    returns largest divisor of n
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1


def minOperations(n):
    """
    minOperations
    returns min operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    largest_divisor = lar_div(n)
    return (n // largest_divisor) + minOperations(largest_divisor)
