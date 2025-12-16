class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        nums = [i*i for i in nums]
        output = [0 for i in range(len(nums))]
        k = len(nums)-1
        while j>=i:
            if nums[j] > nums[i]:
                output[k] = nums[j]
                k -= 1
                j -= 1
            else:
                output[k] = nums[i]
                k -= 1
                i += 1
        return output


