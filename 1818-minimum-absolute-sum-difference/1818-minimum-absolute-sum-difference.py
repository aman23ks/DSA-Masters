class Solution:
    def binarySearch(self, nums1, target):
        l = 0
        h = len(nums1)-1
        while l<=h:
            m = (l+h)//2
            if nums1[m] < target:
                l = m+1
            elif nums1[m] > target:
                h = m-1
            else:
                return nums1[m]
        
        if h < 0:
            return nums1[0]
        if l >= len(nums1):
            return nums1[-1]
        if abs(nums1[h] - target) <= abs(nums1[l] - target):
            return nums1[h]
        return nums1[l]

    def absoluteSumDifference(self, nums1, nums2):
        s = 0
        diff = []
        for i in range(len(nums1)):
            s += abs(nums1[i] - nums2[i])
            diff.append(abs(nums1[i] - nums2[i]))
        
        return [s, diff]


    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = pow(10,9) + 7

        if nums1 == nums2:
            return 0

        res, diff = self.absoluteSumDifference(nums1, nums2)
        
        nums1_sorted = sorted(nums1)

        best = []
        saved = []

        for val in nums2:
            best.append(abs(val-self.binarySearch(nums1_sorted, val)))

        for i in range(len(best)):
            saved.append(diff[i]-best[i])
        
        maxi = max(0, max(saved))
        
        return (res-maxi) % MOD