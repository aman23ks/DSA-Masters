class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left = 0
        right = 0
        n = len(nums)
        for i in range(n):
            if i == 0:
                left += 0
            else:
                left += nums[i-1]
            
            right = s - (left + nums[i])

            if left==right:
                return i
        
        return -1