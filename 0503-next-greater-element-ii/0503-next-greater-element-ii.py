class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        ans = [-1]*len(nums)

        for i in range(len(nums)):
            if st == []:
                st.append([nums[i],i])
                continue
            if st[-1][0] >= nums[i]:
                st.append([nums[i],i])
            else:
                while st and st[-1][0] < nums[i]:
                    val = st.pop()
                    ans[val[1]] = nums[i]
                st.append([nums[i], i])

        for i in range(len(nums)):
            if st[-1][0] >= nums[i]:
                continue
            else:
                while st and st[-1][0] < nums[i]:
                    val = st.pop()
                    ans[val[1]] = nums[i]      

        return ans
