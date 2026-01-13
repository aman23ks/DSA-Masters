class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        i = 0
        n = len(points)
        j = 1
        count = 1
        while j < n:
            a = points[i][1]
            b = points[j][0]
            if a>=b:
                j+=1
            else:
                count += 1
                i = j
                j += 1

        return count