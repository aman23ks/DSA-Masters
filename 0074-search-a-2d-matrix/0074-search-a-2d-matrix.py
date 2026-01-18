class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        while l<=h:
            m = (l+h)//2
            
            if matrix[m][0] == target or matrix[m][-1] == target:
                return True
            
            if matrix[m][0] > target:
                h = m-1
            elif matrix[m][-1] < target:
                l = m+1
            else:
                break
        
        left = 0
        right = len(matrix[0])-1
        while left <= right:
            mid = (left+right)//2
            print(matrix[m][mid])
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False