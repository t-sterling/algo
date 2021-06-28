
from typing import List

import unittest

"""

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

Example 1: 

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000



Example of a general class of problems:
    for a given array and some given conditions, find all combinations in the array

    can this be solved with a sliding window ?
    don't really see how..

"""

class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        # brute force

        r = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] - arr[j] <= a and arr[j] - arr[k] <= b and arr[j] - arr[k] <= c:
                        r += 1

        return r


class TestSolution(unittest.TestCase):

    def test_one(self):

        Solution().countGoodTriplets(
            arr=[3, 0, 1, 1, 9, 7],
            a=7,
            b=2,
            c=3
        )

