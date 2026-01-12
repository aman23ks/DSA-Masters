class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)
        res = [intervals[0]]
        e = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[e][1]:
                res[e][1] = max(res[e][1], intervals[i][1])
            else:
                e += 1
                res.append(intervals[i])
        return res  