class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        hashmap = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1

            diff = zeros - ones
            if diff == 0:
                res = max(res, i+1)
            else:
                if diff not in hashmap:
                    hashmap[diff] = i
                else:
                    res = max(res, i-hashmap[diff])
        
        return res