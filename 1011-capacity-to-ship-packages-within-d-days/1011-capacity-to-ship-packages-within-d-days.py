class Solution:
    def addWeights(self, weights, limit):
        total = 0
        days = 0

        for weight in weights:
            if total + weight > limit:
                days += 1
                total = weight
            else:
                total += weight
        
        return days+1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)
        res = h
        while l<=h:
            m = (l+h)//2
            day = self.addWeights(weights, m)
            if day > days:
                l = m+1
            else:
                res = min(res, m)
                h = m-1

        return res

            
