class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for n in sorted(nums)[::-1]:
            if -n in nums:
                return n
        return -1