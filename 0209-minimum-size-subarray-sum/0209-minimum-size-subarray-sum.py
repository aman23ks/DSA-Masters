from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        s = 0
        mini = float("inf")

        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                mini = min(mini, j - i + 1)
                s -= nums[i]
                i += 1

        return 0 if mini == float("inf") else mini
