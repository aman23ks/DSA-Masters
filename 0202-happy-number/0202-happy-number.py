class Solution:
    def square(self, n: int) -> int:
        s = 0
        while n > 0:
            val = n % 10
            s += (val * val)
            n = n // 10
        return s

    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(self.square(n))
        while slow != fast:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            if slow == 1 and fast == 1:
                return True
        return slow == 1
        