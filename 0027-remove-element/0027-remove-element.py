class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] != val:
                i += 1
                if i == j:
                    if nums[i] != val:
                        return i+1
                #     return i+1
            elif nums[i] == val:
                while nums[j] == val:
                    j -= 1
                    if j < i:
                        return i
                nums[i], nums[j] = nums[j], nums[i]
        return i
        
