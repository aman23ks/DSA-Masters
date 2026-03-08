class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        
    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] != self.min:
            self.min = self.stack[-1][1]
        if self.min == None or self.stack == []:
            self.min = val
        if self.min > val:
            self.min = val
        self.stack.append([val, self.min])

    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack = self.stack[0:-1]

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        mini = self.stack[-1][1]
        return mini
