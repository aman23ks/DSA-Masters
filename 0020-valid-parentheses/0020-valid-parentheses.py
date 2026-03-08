class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        i = 0
        while i < len(s):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] in hashmap:
                stack.append(s[i])
            elif s[i] not in hashmap:
                if stack[-1] in hashmap and hashmap[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
            i += 1
        if len(stack) > 0:
            return False
        return True