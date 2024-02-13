class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        """
        ans = 0
        for k in range(1, len(nums) + 1):
            for i in range(0, len(nums)):
                candidates = nums[i: i+k]
                if len(candidates) == k:
                    ans += len(set(candidates))**2
        return ans
        """
        """
        ans = 0
        for k in range(1, len(nums) + 1):
            for i in range(0, len(nums)):
                if i + k > len(nums):
                    continue
                candidates = nums[i: i+k]
                ans += len(set(candidates))**2
        return ans
        """
        ans = 0
        for k in range(1, len(nums) + 1):
            for i in range(0, len(nums)):
                if i + k <= len(nums):
                    ans += len(set(nums[i: i+k]))**2
        return ans