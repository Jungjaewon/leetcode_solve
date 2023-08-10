class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = nums[0]
        for num in nums[1:]:
            n  *= num
        if n > 0:
            return 1
        elif n < 0:
            return -1
        else:
            return 0