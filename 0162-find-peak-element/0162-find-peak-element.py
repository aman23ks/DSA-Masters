class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l<h:
            m = (l+h)//2
            if nums[m] < nums[m+1]:
                l = m+1
            elif nums[m] < nums[m-1]:
                h = m-1
            else:
                return m
        
        return l
        