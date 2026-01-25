class Solution:
    def binarySearch(self, arr, target):
        l = 0
        h = len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if arr[mid] <= target:
                l = mid+1
            else:
                h = mid-1
    
        return l


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        h = matrix[-1][-1]
        while l<=h:
            m = (l+h)//2
            s = 0
            for mat in matrix:
                s += self.binarySearch(mat, m)
            if s < k:
                l = m+1
            else:
                h = m-1
        
        return l
            
