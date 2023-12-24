class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans = -1
        max_v = max(nums)
        for idx, n in enumerate(nums):
            if n == max_v:
                ans = idx 
                continue
            elif n == 0:
                continue
            else:
                r = max_v / n
                if r < 2.0:
                    ans = - 1
                    break
        return ans