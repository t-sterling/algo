

from typing import List
import math
import unittest

"""

From Introduction To Algorithms. Kadanes Algorithm appears to be simpler - work out time complexity difference

max contiguous sub array problem is to find the sub array where the sum is the greatest
related problem is:
    buy and sell a stock and get the max profit

the max sub array can exist in 
- left sub array 
- right sub-array
- in the middle

case 1 and 2 can be solved as sub problems recursively

case 3 needs special handling, figure out the sub-array on either side of the center
                                                            |
#                   0    1    2    3    4    5    6    7    8    9  10   11   12   13  14  15  16
        prices = [100, 113, 110,  85, 105, 102,  86,  63,  81, 101, 94, 106, 101,  79, 94, 90, 97]
               = [0,    13,  -3, -25,  20,  -3, -16, -23,  18,  20, -7,  12,  -5, -22, 15, -4,  7]
                                                            |-------------|
                                                            |

it's bit hard to follow why the recursion works..


TODO: Kadanes algorithm appears to be a much better approach:
 

"""


def deltas(arr: List[int]):
    ret = [0]
    for i in range(1, len(arr)):
        ret.append(arr[i] - arr[i - 1])
    return ret


def max_crossover(arr: List[int]):

    mid = len(arr) // 2

    # left max start at mid
    #
    left_max = -math.inf    # the running max
    acc = 0                 # the running total
    left = mid              # the position of the max
    for i in range(mid, 0, -1):
        acc += arr[i]
        if acc > left_max:
            left_max = acc
            left = i

    # repeat for the right side
    #
    right_sum = -math.inf
    acc = 0
    right = mid
    for i in range(mid, len(arr)):
        acc += arr[i]
        if acc > right_sum:
            right_sum = acc
            right = i

    return left, right, left_max + right_sum


def find_max(arr: List[int], indent=0):

    print("  " * indent + str(arr))

    # find left, find right, find crossing
    if len(arr) == 1:
        return 0, 1, arr[0]

    else:

        mid = len(arr) // 2

        # left and right are sub problems
        # TODO: I can't understand how it works when the recursion bottoms out..
        #       it will return a single elem array
        left_low, left_high, left_sum = find_max(arr[0: mid], indent+1)

        right_low, right_high, right_sum = find_max(arr[mid: len(arr)], indent+1)

        # crossover needs different handling
        x_low, x_high, x_sum = max_crossover(arr)

        # figure out which result to return
        if left_sum > right_sum and left_sum > x_sum:

            return left_low, left_high, left_sum

        elif right_sum > left_sum and right_sum > x_sum:

            return right_low, right_high, right_sum

        else:

            return x_low, x_high, x_sum


class MaxSubArray(unittest.TestCase):

    def test_delta(self):

        prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

        delts = deltas(prices)

        self.assertEqual(delts, [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])

    def test_crossover(self):

        expected = (8, 11, 61)

        #           0    1    2   3    4    5   6   7   8    9  10   11   12  13  14  15  16
        prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

        delts = deltas(prices)

        actual = max_crossover(delts)

        self.assertEqual(expected, actual)

    def test_example(self):

        expected = (8, 11, 61)

        prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

        delts = deltas(prices)

        actual = find_max(delts)

        self.assertEqual(expected, actual)

    def test_increasing(self):
        # TODO: this answer is wrong
        prices = [1, 2, 3, 4]

        actual = find_max(deltas(prices))

        print(actual)


if __name__ == '__main__':

    unittest.main()

