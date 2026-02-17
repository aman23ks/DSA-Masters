class Solution:
    def check_hashmap(self, hashmap):
        for key in hashmap:
            if hashmap[key] > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        for string in t:
            if string in hashmap:
                hashmap[string] += 1
            else:
                hashmap[string] = 1
        
        i = 0
        j = 0
        length = float('inf')
        result = ""
        
        while j < len(s):
            if s[j] in hashmap:
                hashmap[s[j]] -= 1
            
            while self.check_hashmap(hashmap):
                if length > len(s[i:j+1]):
                    length = len(s[i:j+1])
                    result = s[i:j+1]
                
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    i += 1
                    
                while i<len(s) and s[i] not in hashmap:
                    i+=1
            
            j += 1
        
        return result