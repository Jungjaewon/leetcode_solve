class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        """
        min_v, max_v = min(nums), max(nums)
        for d in nums:
            if d != min_v and d != max_v:
                return d
        return -1
        """
        """
        if len(nums) <= 2:
            return -1
        else:
            nums = sorted(nums)
            return nums[1]
        """
        nums = sorted(nums)
        if len(nums) <= 2:
            return -1
        else:
            return nums[1]