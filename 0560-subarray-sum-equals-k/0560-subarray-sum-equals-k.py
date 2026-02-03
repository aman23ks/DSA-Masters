class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        hashmap = {0:1}
        count = 0
        for i in range(1, len(nums)+1):
            pre_sum += nums[i-1]
            if pre_sum - k in hashmap:
                count += hashmap[pre_sum-k]
            
            if pre_sum not in hashmap:
                hashmap[pre_sum] = 1
            else:
                hashmap[pre_sum] += 1
        
        return count