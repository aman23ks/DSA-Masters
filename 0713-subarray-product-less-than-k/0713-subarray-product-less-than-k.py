class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        ans = 0
        prod = 1
        
        for j in range(len(nums)):
            prod *= nums[j]
            
            # Shrink window while product >= k
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            
            # All subarrays ending at j and starting from i to j
            ans += (j - i + 1)
        
        return ans