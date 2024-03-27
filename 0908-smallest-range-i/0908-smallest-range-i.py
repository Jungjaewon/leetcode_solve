class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_v, max_v = min(nums), max(nums)
        
        ret = (max_v - k) - (min_v + k)
        
        if ret < 0:
            return 0
        else:
            return ret