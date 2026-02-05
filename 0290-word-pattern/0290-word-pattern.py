class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(pattern) != len(s):
            return False
        
        hashmap_1 = {}
        hashmap_2 = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in hashmap_1:
                hashmap_1[pattern[i]] = s[i]
            
            if s[i] not in hashmap_2:
                hashmap_2[s[i]] = pattern[i]
            
            if hashmap_1[pattern[i]] != s[i] or hashmap_2[s[i]] != pattern[i]:
                return False

        return True