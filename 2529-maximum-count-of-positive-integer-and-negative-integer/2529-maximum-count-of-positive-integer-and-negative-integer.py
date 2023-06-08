class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum([1 for n in nums if n > 0]), sum([1 for n in nums if n < 0]))