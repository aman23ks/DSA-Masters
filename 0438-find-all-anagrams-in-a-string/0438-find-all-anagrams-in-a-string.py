class Solution:
    def check(self, hashmap):
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = 0
        n = len(s)
        k = len(p)
        hashmap = {}
        output = []
        for val in p:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1
        
        new_map = hashmap.copy()

        while j < n:
            if self.check(new_map):
                output.append(i)

            if j - i < k:
                if s[j] not in new_map:
                    j += 1
                else:
                    new_map[s[j]] -= 1
                    j += 1
            else:
                if s[i] not in new_map:
                    i += 1
                else:
                    new_map[s[i]] += 1
                    i += 1
            
        if self.check(new_map):
            output.append(i)

        return output
