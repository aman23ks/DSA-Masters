class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        while l<=h:
            m = (l+h)//2
            s = 0
            c = 1
            for i in nums:
                if s + i <= m:
                    s += i
                else:
                    c += 1
                    s = i

            if c > k:
                l = m+1
            else:
                h = m-1
        
        return l