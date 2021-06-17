
from typing import List
import random

"""
reference merge sort. works by splitting the input list recursively into smaller arrays then merges them on the way back up
runtime is n log n
"""


def merge_sort(unsorted: List[int], depth=0):

    def split(to_split: List[int]):
        mid = int(len(to_split) / 2)
        return to_split[0:mid], to_split[mid:len(to_split)]

    # note: this merge method is generally useful outside of this.
    #
    def merge(left: List[int], right:List[int]):

        out = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                out.append(left.pop(0))
            else:
                out.append(right.pop(0))

        while len(left) > 0:
            out.append(left.pop(0))

        while len(right) > 0:
            out.append(right.pop(0))

        return out

    if len(unsorted) == 1:

        return unsorted

    else:

        l, r = split(unsorted)
        print(("   " * depth) + str(l) + " | " + str(r))
        merged = merge(merge_sort(l, depth + 1), merge_sort(r, depth + 1))
        print(("   " * depth) + str(merged))
        return merged


if __name__ == "__main__":

    unsorted_ints = random.sample(range(1, 100), 20)

    print(unsorted_ints)
    sorted_ints = merge_sort(unsorted_ints)
    print(sorted_ints)

