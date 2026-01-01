class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = 0
        hashmap = {}
        for i in range(right+1):
            prefix_sum += self.nums[i]
            hashmap[i] = prefix_sum

        if left == 0:
            return hashmap[right]
        return hashmap[right] - hashmap[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)