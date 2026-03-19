class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if stack == []:
                stack.append(asteroids[i])
                continue
            if stack and (not (stack[-1] < 0 and asteroids[i] < 0) or not (stack[-1] > 0 and asteroids[i] > 0)):
                if stack[-1] < 0 and asteroids[i] > 0:
                    stack.append(asteroids[i])
                elif (stack[-1] > 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] < 0):
                    stack.append(asteroids[i])
                elif abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                elif abs(asteroids[i]) > abs(stack[-1]):
                    while stack and abs(asteroids[i]) > abs(stack[-1]) and ((stack[-1] > 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0)) :
                        stack.pop()
                    if stack and abs(asteroids[i]) < abs(stack[-1]) and ((stack[-1] > 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0)):
                        continue
                    if stack and abs(asteroids[i]) == abs(stack[-1]) and ((stack[-1] > 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0)):
                        stack.pop()
                        continue
                    stack.append(asteroids[i])
                        
        return stack