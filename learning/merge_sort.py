
"""
reference for an often useful function
"""
from typing import List


def merge(a: List, b: List) -> List:

    a_sorted = sorted(a)
    b_sorted = sorted(b)

    a_max = len(a)
    b_max = len(b)

    l = []
    a_i = 0
    b_i = 0

    while a_i < a_max or b_i < b_max:

        if a_i < a_max and b_i >= b_max:
            l.append(a_sorted[a_i])
            a_i += 1
        elif b_i < b_max and a_i >= a_max:
            l.append(b_sorted[b_i])
            b_i += 1

        else:
            if a_sorted[a_i] < b_sorted[b_i]:
                l.append(a_sorted[a_i])
                a_i += 1
            else:
                l.append(b_sorted[b_i])
                b_i += 1

    return l


if __name__ == "__main__":

    print(merge([2], [1]))

    print(merge([3, 1, 6], [4, 2, 5]))
