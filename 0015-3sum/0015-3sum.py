class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        j = i + 1
        k = len(nums)-1
        s = 0
        while i < len(nums)-2:
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                while j+1 < len(nums) and j+1 <= k and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            elif s > 0:
                while k-1 > 0 and k-1 >= j and nums[k-1] == nums[k]:
                    k -= 1
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                while j+1 < len(nums) and j+1 <= k and nums[j+1] == nums[j]:
                    j += 1
                j += 1
                while k-1 > 0 and k-1 >= j and nums[k-1] == nums[k]:
                    k -= 1
                k -= 1
            
            if j >= k:
                while i+1 < len(nums) and nums[i+1] == nums[i]:
                    i+=1
                i+=1
                j = i+1
                k = len(nums)-1
        
        return result