class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        length = 0
        maxi = 0
        hashmap = dict()
        while r<len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
                length = r-l+1
                r += 1
                maxi = max(length, maxi)
            else:
                if hashmap[s[r]] >= l:
                    l = hashmap[s[r]] + 1
                hashmap[s[r]] = r
                length = r-l+1
                maxi = max(length, maxi)
                r+=1
        return maxi
    
                