class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return m
        
            if nums[m] > target:
                h = m-1
            else:
                l = m+1
        
        if nums[m] < target:
            return m + 1
        elif nums[m] > target:
            if m - 1 < 0:
                return 0 
            return m