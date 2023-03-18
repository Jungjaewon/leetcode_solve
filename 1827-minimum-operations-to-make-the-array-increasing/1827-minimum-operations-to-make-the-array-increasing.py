class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                gap = abs(nums[i] - nums[i + 1]) + 1
                ans += gap
                nums[i + 1] = nums[i + 1] + gap
        return ans
        """
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                gap = nums[i] - nums[i + 1] + 1
                ans += gap
                nums[i + 1] += gap
        return ans