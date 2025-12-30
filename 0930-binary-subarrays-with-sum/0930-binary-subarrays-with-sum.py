class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0:1}
        for i in range(1, len(nums)+1):
            prefix_sum += nums[i-1]
            if prefix_sum - goal in hashmap:
                count += hashmap[prefix_sum - goal] 
            
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = 1
            else:
                hashmap[prefix_sum] += 1
        
        return count