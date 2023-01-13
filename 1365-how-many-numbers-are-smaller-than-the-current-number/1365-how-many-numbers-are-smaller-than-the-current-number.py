class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = list()
        for num in nums:
            ans.append(sum([1 for n in nums if num > n]))
        return ans