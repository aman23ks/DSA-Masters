class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        st = []
        ans = []

        for i in nums2:
            if st == []:
                st.append(i)
                continue

            if st[-1] > i:
                st.append(i)
            else:
                while st and st[-1] < i:
                    hashmap[st.pop()] = i
                st.append(i)
        
        while st:
            hashmap[st.pop()] = -1
        
        for i in nums1:
            ans.append(hashmap[i])

        return ans