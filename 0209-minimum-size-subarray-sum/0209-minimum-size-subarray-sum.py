class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        s = 0
        count = 0
        min_len = float("inf")
        while j < len(nums):
            if s < target:
                s += nums[j]
                j += 1
                count += 1
            else:
                min_len = min(min_len, count)
                count -= 1
                s -= nums[i]
                i += 1

        while i < len(nums):
            if s >= target:
                min_len = min(min_len, count)
                s -= nums[i]
                count -= 1
                i += 1
            else:
                i += 1
            
        if min_len == float("inf"):
            return 0
                                
        return min_len


