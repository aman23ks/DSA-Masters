class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        i = 0
        j = 0
        while i<len(s):
            if s[i] == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
            
            i += 1
        
        while j<len(t):
            if t[j] == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[j])
            
            j += 1

        return stack_s == stack_t