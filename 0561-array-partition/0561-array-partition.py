class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        ans = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            ans += min(nums[i], nums[i + 1])
        return ans
        """
        nums = sorted(nums)
        return sum([ min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2) ])