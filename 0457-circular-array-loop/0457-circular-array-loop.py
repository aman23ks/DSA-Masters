class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow, fast = i, nxt(i)

            while (
                nums[slow] != 0 and nums[fast] != 0 and nums[nxt(fast)] != 0 and
                (nums[slow] > 0) == direction and
                (nums[fast] > 0) == direction and
                (nums[nxt(fast)] > 0) == direction
            ):
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    return True

                slow = nxt(slow)
                fast = nxt(nxt(fast))

            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == direction:
                nxt_curr = nxt(curr)
                nums[curr] = 0
                curr = nxt_curr

        return False
