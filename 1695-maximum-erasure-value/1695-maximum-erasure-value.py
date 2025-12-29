class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        maxi = 0
        hashmap = {}
        n = len(nums)
        for val in nums:
            if val not in hashmap:
                hashmap[val] = 0
    
        while j < n:
            hashmap[nums[j]] += 1
            while hashmap[nums[j]] > 1:
                count -= nums[i]
                hashmap[nums[i]] -= 1
                i += 1
    
            count += nums[j]
            maxi = max(maxi, count)

            j += 1
        
        return maxi