class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
        """
        ans,nums = 0, sorted(list(set(nums)))
        while not all([0 == n for n in nums]):
            nums = [n for n in nums if n > 0]
            nums = [n - nums[0] for n in nums]
            ans += 1
        return ans
        """
        """
        ans = 0
        while not all([0 == n for n in nums]):
            min_v = [n for n in sorted(nums) if n != 0][0]
            nums = [n - min_v if n - min_v > 0 else 0 for n in nums]
            ans += 1
        return ans
        """