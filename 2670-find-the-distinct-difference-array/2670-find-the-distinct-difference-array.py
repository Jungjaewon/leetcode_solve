class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = len(set(nums[:i + 1])) - len(set(nums[i + 1:]))
        return ans