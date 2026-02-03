class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = [s]
            else:
                hashmap[sorted_s].append(s)
        
        output = []
        for key, values in hashmap.items():
            output.append(values)

        return output