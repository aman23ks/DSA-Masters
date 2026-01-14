class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        a,b = intervals[0]
        total = len(intervals)
        for i in range(1, len(intervals)):
            c, d = intervals[i]
            if a <= c and d <= b:
                total -= 1
            else:
                a = c
                b = d

        return total
