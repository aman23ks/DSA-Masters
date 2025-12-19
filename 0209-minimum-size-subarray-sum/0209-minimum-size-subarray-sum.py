class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        length = 0
        s = 0
        mini = float("inf")
        while j<len(nums):
            if s<target:
                s+=nums[j]
                length += 1
                j += 1
            else:
                mini = min(length, mini)
                s -= nums[i]
                i += 1
                length -= 1
        
        while i<len(nums):
            if s >= target:
                mini = min(length, mini)
            s -= nums[i]
            i += 1
            length -= 1
        
        if mini == float("inf"):
            return 0
        return mini
