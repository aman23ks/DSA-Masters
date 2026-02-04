class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_1 = {}
        hashmap_2 = {}

        for i in range(len(s)):
            if s[i] not in hashmap_1:
                hashmap_1[s[i]] = t[i]
            if t[i] not in hashmap_2:
                hashmap_2[t[i]] = s[i]
            
            if hashmap_1[s[i]] != t[i] or hashmap_2[t[i]] != s[i]:
                return False

        return True