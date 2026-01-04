class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = pow(10, 9) + 7
        even = 1
        odd = 0
        pre = 0
        ans = 0
        for i in arr:
            pre += i
            if pre % 2 == 0:
                ans += odd
                even += 1
            else:
                ans+=even
                odd += 1
        return ans%MOD
