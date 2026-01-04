class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                best = max(best, 2*left)
            elif right > left:
                left = 0
                right = 0
        
        left, right = 0, 0
        for i in reversed(s):
            if i == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                best = max(best, 2*left)
            elif left > right:
                left = 0
                right = 0
        
        return best

