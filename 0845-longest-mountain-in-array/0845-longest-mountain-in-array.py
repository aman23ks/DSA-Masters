class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)

        if (n < 3):
            return 0
        
        left = 0
        right = 0
        maxi = 0
        for i in range(1, n-1):
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                left = i
                right = i
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1
                
                maxi = max(maxi, right-left+1)
        return maxi