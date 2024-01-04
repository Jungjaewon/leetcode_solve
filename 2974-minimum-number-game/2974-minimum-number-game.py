class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = [[nums[i +1], nums[i]] for i in range(0,len(nums), 2)]
        ans = [ y for x in ans for y in x]
        return ans
        