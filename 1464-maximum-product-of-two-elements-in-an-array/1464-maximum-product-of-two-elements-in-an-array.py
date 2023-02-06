class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        ans = -10e4
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n = (nums[i] - 1) * (nums[j] - 1)
                ans = max(ans, n)
        return ans
        """
        nums = sorted(nums)
        return (nums[-1] - 1) * (nums[-2] - 1)