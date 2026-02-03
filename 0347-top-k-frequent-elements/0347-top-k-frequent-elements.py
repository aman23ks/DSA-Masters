class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for val in nums:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1
        
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        return list(hashmap.keys())[:k]
        
        