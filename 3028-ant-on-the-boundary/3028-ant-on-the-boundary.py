class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return len([1 for n in nums if n == 0])
        """
        nums = list(accumulate(nums))
        return len([1 for n in nums if n == 0])
        