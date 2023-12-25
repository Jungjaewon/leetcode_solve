class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp_l = nums[j + 1:]
                t = 0 if len(temp_l) == 0 else max(temp_l)
                ans = max(ans, (nums[i] - nums[j]) * t)
        return ans