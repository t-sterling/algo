"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates
 where the chosen numbers sum to target. You may return the combinations in any order.

The same math may be chosen from candidates an unlimited math of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the math of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

recursive solution: start with target and for each elem of candidates, subtract candidates[i] from target and recurse.
                    if target is 0 then solution is found
                    if target < 0 then move on to next i

"""

from typing import List


def solve(candidates: List[int], target):

    def inner(_candidates: List[int], comb: List[int], _target) -> List[List[int]]:

        combinations = []

        for i in range(len(_candidates)):

            c = _candidates[i]

            comb.append(c)
            r = _target - c

            if r > 0:
                for c in inner(_candidates[i+1:], comb, r):
                    combinations.append(c)

            if r == 0:
                combinations.append(comb.copy())

            comb.pop()

        return combinations

    return inner(candidates, [], target)


if __name__ == "__main__":

    solve([2, 3, 6, 7], 7)

    solve([2, 3, 5], 8)
