from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        i = 0
        j = 0
        n = len(nums)
        ans = []
        dq = deque()
        while j < n:
            if j - i < k:
                if not dq:
                    dq.append(j)
                elif nums[dq[0]] < nums[j]:
                    while dq:
                        dq.pop()
                    dq.append(j)
                else:
                    while nums[j] > nums[dq[-1]]:
                        dq.pop()
                    dq.append(j)
                j += 1
            else:
                ans.append(nums[dq[0]])
                if dq[0] == i:
                    dq.popleft()
                i += 1
        ans.append(nums[dq[0]])
        return ans
