class Solution:
    def all_equal_zero(self, hashmap):
        for c in hashmap:
            if hashmap[c] != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        i = 0
        j = 0
        hashmap = {}
        for val in s1:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1
                
        while j < n:
            if self.all_equal_zero(hashmap):
                return True
            if j-i < k:
                if s2[j] not in hashmap:
                    j += 1
                else:
                    hashmap[s2[j]] -= 1
                    j += 1
            else:
                if s2[i] not in hashmap:
                    i += 1
                else:
                    hashmap[s2[i]] += 1
                    i += 1
        
        if self.all_equal_zero(hashmap):
            return True
        return False
