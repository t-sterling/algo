
from typing import List
import random

"""
reference insertion sort. works by splitting the input list recursively into smaller arrays then merges them on the way back up
runtime is n ** 2
inuitively it's the way people sort cards in the hand

"""


def insertions_sort(unsorted: List[int]):

    for i in range(1, len(unsorted)):
        k = unsorted[i]
        j = i - 1
        while unsorted[j] > k and j >= 0:
            unsorted[j+1] = unsorted[j]
            j -= 1
        unsorted[j+1] = k

    return unsorted


if __name__ == "__main__":

    unsorted_ints = random.sample(range(1, 100), 20)
    print(unsorted_ints)
    sorted_ints = insertions_sort(unsorted_ints)
    print(sorted_ints)

