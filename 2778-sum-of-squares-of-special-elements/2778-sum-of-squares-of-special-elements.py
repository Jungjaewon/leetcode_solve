class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            if len(nums) % (idx + 1) == 0:
                ans += (nums[idx] * nums[idx])
        return ans