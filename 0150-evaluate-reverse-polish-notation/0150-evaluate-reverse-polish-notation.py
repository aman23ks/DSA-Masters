class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "/", "-", "*"]:
                stack.append(tokens[i])
            else:
                if tokens[i] == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num1) + int(num2))
                elif tokens[i] == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num1) * int(num2))
                elif tokens[i] == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2) - int(num1))
                elif tokens[i] == "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(int(num2) / int(num1)))
        
        return int(stack[0])