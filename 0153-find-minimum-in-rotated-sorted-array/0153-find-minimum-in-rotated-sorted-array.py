class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l<h:
            m = (l+h)//2
            if nums[m] >= nums[h]:
                l = m+1
            elif nums[m] <= nums[l]:
                h = m
            else:
                break

        return nums[l]