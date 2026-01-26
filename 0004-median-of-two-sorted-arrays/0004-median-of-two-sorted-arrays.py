class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        if len(nums1) > len(nums2):
            h = len(nums2)
        else:
            h = len(nums1)
        
        l = 0

        while l<=h:
            m1 = (l+h)//2
            m2 = n//2-m1
            l1 = None
            l2 = None
            r1 = None
            r2 = None
            
            l1 = nums1[m1 - 1] if m1 - 1 >= 0 else None
            r1 = nums1[m1] if m1 < len(nums1) else None

            l2 = nums2[m2 - 1] if m2 - 1 >= 0 else None
            r2 = nums2[m2] if m2 < len(nums2) else None

            if l1 is not None and r2 is not None and l1 > r2:
                h = m1 - 1
            elif l2 is not None and r1 is not None and l2 > r1:
                l = m1 + 1
            else:
                break

            if l1 and r2 and l1 > r2:
                h = m1-1
            elif l2 and r1 and l2 > r1:
                l = m1+1
            else:
                break
        
        if l1 is None:
            l1 = float('-inf')
        if l2 is None:
            l2 = float('-inf')
        if r1 is None:
            r1 = float('inf')
        if r2 is None:
            r2 = float('inf')
        return (max(l1,l2) + min(r1,r2))/2 if n%2 == 0 else min(r1,r2)