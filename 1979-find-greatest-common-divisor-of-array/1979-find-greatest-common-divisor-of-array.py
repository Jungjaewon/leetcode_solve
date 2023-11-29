class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_v, min_v = max(nums), min(nums)
        for i in range(max_v, 0, -1):
            if min_v % i == 0 and max_v % i == 0:
                return i