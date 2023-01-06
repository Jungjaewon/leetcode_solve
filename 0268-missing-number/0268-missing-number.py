class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return [i for i in range(len(nums) + 1) if i not in nums][0]
        #for i in range(len(nums) + 1):
        #    if i not in nums:
        #        return i
        #return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)