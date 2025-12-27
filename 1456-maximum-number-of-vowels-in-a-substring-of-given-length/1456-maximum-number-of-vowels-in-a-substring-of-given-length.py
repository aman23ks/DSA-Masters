class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        vowel = 0
        n = len(s)
        maxi = 0
        while j < n:
            if j-i < k:
                if s[j] in vowel_list:
                    vowel += 1
                    maxi = max(maxi, vowel)
                j += 1
            else:
                if s[i] in vowel_list:
                    vowel -= 1
                i += 1
        return maxi