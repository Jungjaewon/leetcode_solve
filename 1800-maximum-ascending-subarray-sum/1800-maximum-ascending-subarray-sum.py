class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = -10e4
        idx = 0
        while idx < len(nums):
            temp = 0
            while idx + 1 < len(nums) and nums[idx] < nums[idx + 1]:
                temp += nums[idx]
                idx += 1
            temp += nums[idx]
            ans = max(ans, temp)
            idx += 1
        return max(ans, temp)