class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        for i in range(len(nums)):
            if nums[i] == nums[j-1]:
                continue
            elif nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
        return j