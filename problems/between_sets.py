
"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

"""

import functools


def gcd(i: int, j: int) -> int:

    while j != 0:

        (i, j) = (j, i % j)

    return i


def lcm(i: int, j: int) -> int:

    return int(i * j / gcd(i, j))


def between_sets(first, second):

    l = functools.reduce(lambda a, b: lcm(a, b), first)

    g = functools.reduce(lambda a, b: gcd(a, b), second)

    return int(g / l)


if __name__ == "__main__":

    print(between_sets([2, 6], [24, 36]))
