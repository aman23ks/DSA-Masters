class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        val = nums[0]
        start = nums[0]
        output = []
        for i in range(1, len(nums)):
            if nums[i] == (val + 1):
                val = nums[i]
                continue
            else:
                if start == val:
                    output.append(f"{start}")
                    start = nums[i]
                    val = nums[i]
                else:
                    output.append(f"{start}->{val}")
                    start = nums[i]
                    val = nums[i]
        
        if nums[-1] == (val + 1):
            val = nums[-1]
        else:
            if start == val:
                output.append(f"{start}")
                start = nums[-1]
                val = nums[-1]
            else:
                output.append(f"{start}->{val}")
                start = nums[-1]
                val = nums[-1]
        
        return output