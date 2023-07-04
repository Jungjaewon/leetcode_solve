class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_v, max_v = min(nums), max(nums)
        for d in nums:
            if d != min_v and d != max_v:
                return d
        return -1