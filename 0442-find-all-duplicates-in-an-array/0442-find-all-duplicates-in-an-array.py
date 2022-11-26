class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        idx, ans = 0, []
        while idx < len(nums):
            if idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                ans.append(nums[idx])
            idx += 1
        return ans
        """
        from collections import Counter
        return [key for key, val in Counter(nums).items() if val > 1]
        """