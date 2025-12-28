class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        count = 0
        maxi = 0
        zeros_flipped = 0
        while j < n:
            if nums[j] == 1:
                count += 1
                j += 1
            else:
                if zeros_flipped != k:
                    zeros_flipped += 1
                    count += 1
                    j += 1
                else:
                    maxi = max(count, maxi)
                    while zeros_flipped == k:
                        if nums[i] == 1:
                            i += 1
                            count -= 1
                        else:
                            zeros_flipped -= 1
                            count -= 1
                            i += 1
        maxi = max(count, maxi)
        return maxi