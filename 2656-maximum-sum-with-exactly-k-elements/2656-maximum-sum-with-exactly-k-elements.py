class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        """
        base = max(nums)
        return sum([ base + i for i in range(k)])
        """
        base = sorted(nums)[-1]
        return sum([ base + i for i in range(k)])