from typing import List

"""
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

TODO: this is just a special case of combination-sum

"""


class Solution:

    # for every math in 4sum does target-n 3sum exist?
    # for every math in 3sum does target-n 2sum exist?

    def twoSum(self, nums: List[int], two_target: int) -> List[int]:

        two_cache = set()
        for n in nums:
            if two_target - n in two_cache:
                return [n, two_target - n]
            two_cache.add(n)

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret: List[List[int]] = list()

        _nums = list(nums)
        while len(_nums) > 0:
            n = _nums.pop()
            twos = self.twoSum(list(_nums), target - n)
            if twos is not None:
                twos.append(n)
                ret.append(twos)

        return ret

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret: List[List[int]] = list()

        _nums = list(nums)
        while len(_nums) > 0:
            n = _nums.pop()
            threes = self.threeSum(list(_nums), target - n)
            if len(threes) > 0:
                for l in threes:
                    l.append(n)
                    ret.append(l)

        return ret


if __name__ == "__main__":

    s = Solution()

    print(s.fourSum([1,0, -1, 0, -2, 2], 0))

    print(s.fourSum([2,2,2,2,2], 8))
