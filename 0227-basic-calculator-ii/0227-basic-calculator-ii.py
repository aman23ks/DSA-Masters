class Solution:
    def val_calculate(self, val1, val2, op):
        val1 = int(val1)
        val2 = int(val2)
        if op == "+":
            return val1 + val2
        elif op == "-":
            return val2 - val1
        elif op == "*":
            return val1 * val2
        elif op == "/":
            return int(val2 / val1)

    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        priority = {"/": 2, "*": 2, "+": 1, "-": 1}
        sign = None

        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1

            val = ""
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1

            if val != "":
                stack.append(val)

            if i < len(s) and s[i] in ["/", "*", "+", "-"]:
                if sign == None:
                    stack.append(s[i])
                    sign = s[i]
                else:
                    while len(stack) >= 3 and priority[stack[-2]] >= priority[s[i]]:
                        val1 = stack.pop()
                        op = stack.pop()
                        val2 = stack.pop()
                        stack.append(str(self.val_calculate(val1, val2, op)))

                    stack.append(s[i])
                    sign = s[i]

            i += 1

        # first reduce remaining * and /
        new_stack = [stack[0]]
        j = 1
        while j < len(stack):
            op = stack[j]
            num = stack[j + 1]
            if op in ["*", "/"]:
                prev = new_stack.pop()
                new_stack.append(str(self.val_calculate(num, prev, op)))
            else:
                new_stack.append(op)
                new_stack.append(num)
            j += 2

        # then reduce + and -
        res = int(new_stack[0])
        j = 1
        while j < len(new_stack):
            op = new_stack[j]
            num = int(new_stack[j + 1])
            if op == "+":
                res += num
            else:
                res -= num
            j += 2

        return res