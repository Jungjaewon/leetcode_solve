class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for idx, n in enumerate(nums):
            if idx + 1 != len(nums) and nums[idx] == nums[idx + 1]:
                nums[idx] = nums[idx] * 2
                nums[idx + 1] = 0
        return [n for n in nums if n != 0] + [0 for n in nums if n == 0]