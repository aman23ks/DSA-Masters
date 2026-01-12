class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1] and newInterval[1] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0] and newInterval[1] < intervals[i][1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                intervals[i][0] = min(intervals[i][0], newInterval[0])
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                newInterval = intervals[i]
        res.append(newInterval)
        return res