
import functools
from typing import List


def find_non_duplicate(items: List[int]):

    i = functools.reduce(lambda a, b: a ^ b, items)

    print(i)


if __name__ == "__main__":

    find_non_duplicate([1, 2, 2, 1, 57])

