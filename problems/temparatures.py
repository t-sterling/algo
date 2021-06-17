
from typing import List

"""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is
the math of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100


"""

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        pass