class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        r_max = []
        l = height[0]
        r = height[-1]
        l_max.append(height[0])
        r_max.append(height[-1])
        total = 0
        for i in height:
            l = max(l, i)
            l_max.append(l)
        for i in range(len(height)-1, -1, -1):
            r = max(r, height[i])
            r_max.append(r)
        r_max = r_max[::-1]
        for i in range(len(height)):
            if height[i] < l_max[i] and height[i] < r_max[i]:
                total += min(l_max[i], r_max[i]) - height[i]
        return total