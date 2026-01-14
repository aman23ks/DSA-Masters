class Solution:
    def binarySearch(self, low, high, target, intervals):
        while low <= high:
            mid = (low+high)//2
            if intervals[mid][0][0] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([(intervals[i], i) for i in range(len(intervals))])
        res = []
        for i in range(len(intervals)):
            res.append([intervals[i][1], self.binarySearch(i, len(intervals)-1, intervals[i][0][1], intervals)])
        
        ans = []
        res = sorted(res)
        for i in res:
            ans.append(-1 if i[1] == len(intervals) else intervals[i[1]][1])
        return ans