class Solution:
    def update_max_freq(self, hashmap, maxfreq):
        for i in hashmap:
            if hashmap[i] > maxfreq:
                maxfreq = hashmap[i]
        return maxfreq

    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        maxlen = 0
        maxfreq = 0
        n = len(s)
        hashmap = {}
        ans = 0
        for c in s:
            if c not in hashmap:
                hashmap[c] = 0

        while j < n:
            hashmap[s[j]] += 1
            maxfreq = self.update_max_freq(hashmap, maxfreq)
            if ((j-i+1) - maxfreq) <= k:
                j += 1
                maxlen += 1
                ans = max(maxlen, ans)
            else:
                hashmap[s[j]] -= 1 
                hashmap[s[i]] -= 1
                i += 1
                maxlen -=1
        
        return ans