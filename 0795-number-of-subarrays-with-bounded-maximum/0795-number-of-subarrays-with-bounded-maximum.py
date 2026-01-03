class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_max_leq(val):
            streak = 0
            total = 0
            for i in nums:
                if i<=val:
                    streak += 1
                else:
                    streak = 0
                total += streak
            return total
        
        return count_max_leq(right) - count_max_leq(left-1)