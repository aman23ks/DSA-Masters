class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_left = [0]*len(nums)
        prefix_right = [0]*len(nums)
        for i in range(1, len(nums)):
            prefix_left[i] = prefix_left[i-1] + nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            prefix_right[i] = prefix_right[i+1] + nums[i+1]

        for i in range(len(nums)):
            if prefix_left[i] == prefix_right[i]:
                return i
        return -1