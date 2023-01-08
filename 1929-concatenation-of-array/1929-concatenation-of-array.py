class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums + nums
        nums.extend(nums)
        return nums