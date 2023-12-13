class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 10e4
        for idx, n in enumerate(nums):
            if n == target:
                ans = min(abs(idx - start), ans)
        return ans
        