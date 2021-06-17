"""
find the minimum number of swaps of an unordered array to order it

idea is that you count the cycle of values to indexes

"""

import unittest


def count_swaps_1(arr):
    """
    :param arr:
    :return:
    """

    swap_count = 0

    # for each elem ...
    #
    for i in range(len(arr)):

        # while it's value is not the same as it's index, swap it with the value at arr[arr[i]]
        #
        while arr[i] != (i+1):
            v = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = v
            swap_count += 1

    return swap_count


class TestCountSwap(unittest.TestCase):

    def test_one_swap(self):

        actual = count_swaps_1([1, 4, 3, 2])

        self.assertEqual(1, actual)

    def test_two_swaps(self):

        actual = count_swaps_1([1, 4, 2, 3])

        self.assertEqual(2, actual)
