class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        sorted_bloomDay = sorted(bloomDay)
        l = 0
        h = len(sorted_bloomDay)-1

        flowers_bloomed = [0 for i in bloomDay]
        min_days = float('inf')

        while l<=h:
            mid = (l+h)//2
            
            if mid+1 < m*k:
                l = mid + 1
            else:
                for i in range(len(bloomDay)):
                    if bloomDay[i] <= sorted_bloomDay[mid]:
                        flowers_bloomed[i] = 1
                
                count_k = 0
                count_m = 0
                for i in flowers_bloomed:
                    if i == 1:
                        count_k+=1
                        if count_k == k:
                            count_m+=1
                            count_k = 0
                    else:
                        count_k = 0
                
                if count_m >= m:
                    min_days = min(min_days, sorted_bloomDay[mid])
                    h = mid - 1
                    flowers_bloomed = [0 for i in bloomDay]
                else:
                    flowers_bloomed = [0 for i in bloomDay]
                    l = mid+1

        return min_days if min_days != float('inf') else -1