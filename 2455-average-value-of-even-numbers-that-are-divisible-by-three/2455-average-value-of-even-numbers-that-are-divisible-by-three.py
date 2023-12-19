class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [x for x in nums if x % 3 == 0 and x & 1 == 0]
        return int(sum(nums) / (len(nums) + 1 if len(nums) == 0 else len(nums)))