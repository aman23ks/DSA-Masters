class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_first_index = {0:-1}
        pre = 0
        for i,x in enumerate(nums):
            pre += x
            rem = pre%k

            if rem in rem_first_index:
                if i - rem_first_index[rem] >= 2:
                    return True
            else:
                rem_first_index[rem] = i
        return False