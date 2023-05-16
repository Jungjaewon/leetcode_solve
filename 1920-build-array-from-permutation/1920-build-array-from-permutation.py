class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        ans, cnt = list(), 0
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        """
        ans = list()
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans