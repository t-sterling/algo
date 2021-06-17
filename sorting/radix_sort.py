
from typing import List
import random

"""
reference radix sort: works by bucketing from the most significant digit down to the smallest
runtime is K * n where K is the radix
is faster than comparison sorts but requires we know something about the input. 

"""


def radix_sort(unsorted: List[int]):

    def find_radix(ints: List[int]) -> int:
        m = max(ints)
        r = 1
        while m > 0:
            m = m // 10 ** r
            r += 1
        return r

    def sort(ints: List[int], r: int) -> List[int]:
        out: List[List[int]] = [[] for _ in range(10)]
        for i in ints:
            # isolate the digit of the num we care about
            out[(i % 10 ** r) // (10 ** (r-1))].append(i)
        return [item for sub in out for item in sub]

    # runtime: k * n
    for k in range(find_radix(unsorted)):
        unsorted = sort(unsorted, k+1)

    return unsorted


if __name__ == "__main__":

    test_input = random.sample(range(0, 999), 50)
    print(test_input)
    output = radix_sort(test_input)
    print(output)
