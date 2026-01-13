class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)
        res = []

        while i<n and j<m:
            if firstList[i][0] > secondList[j][1]:
                j += 1
            elif secondList[j][0] > firstList[i][1]:
                i += 1
            elif firstList[i][0] <= secondList[j][0] and firstList[i][1] >= secondList[j][1]:
                res.append([secondList[j][0], secondList[j][1]])
                j += 1
            elif secondList[j][0] <= firstList[i][0] and secondList[j][1] >= firstList[i][1]:
                res.append([firstList[i][0], firstList[i][1]])
                i += 1
            elif firstList[i][1] >= secondList[j][0] and firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                res.append([secondList[j][0], firstList[i][1]])
                i += 1
            elif secondList[j][1] >= firstList[i][0] and secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                res.append([firstList[i][0], secondList[j][1]])
                j += 1
        
        return res