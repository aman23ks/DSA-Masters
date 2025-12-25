class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i = 0
        j = 0
        avg = float("-inf")
        s = 0
        while j<n:
            if j-i<k:
                s+=nums[j]
                j+=1
            else:
                avg = max(avg, s/k)
                s -= nums[i]
                i += 1
        
        avg = max(avg, s/k)
        
        return avg