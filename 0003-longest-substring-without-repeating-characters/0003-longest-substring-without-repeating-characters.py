class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        maxlen = 0
        hashmap = {}
        start = 0  # To keep track of the start of the window
        
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= start:
                start = hashmap[s[i]] + 1  # Move the start to the right of the previous occurrence
            
            hashmap[s[i]] = i  # Update the last seen index of the character
            maxlen = max(maxlen, i - start + 1)  # Update the max length of the window

        return maxlen