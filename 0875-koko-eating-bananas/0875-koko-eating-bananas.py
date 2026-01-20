import math

class Solution:
    def check_hours(self, bananas, piles):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/bananas)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        l = 1
        res = hi
        while l<=hi:
            m = (l+hi)//2
            val = self.check_hours(m, piles) 
            if val > h:
                l = m+1
            elif val <= h:
                res = min(res, m)
                hi = m-1
        return res

        