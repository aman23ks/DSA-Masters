class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float("-inf")
        prefix_sums = [0]
        s = 0
        for i in range(1, len(nums)+1):
            s += nums[i-1]
            prefix_sums.append(s)
        
        for i in range(len(nums)-k+1):
            maxi = max(maxi, prefix_sums[i+k] - prefix_sums[i])
        
        return maxi/k
