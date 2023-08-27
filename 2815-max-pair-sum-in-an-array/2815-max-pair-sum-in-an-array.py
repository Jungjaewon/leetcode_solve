class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        for a, b in list(combinations(nums, 2)):
            if sorted(list(str(a)))[-1] == sorted(list(str(b)))[-1]:
                ans = max(ans, a + b)
        return ans