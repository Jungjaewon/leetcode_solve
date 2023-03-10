class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        #while original in nums:
        #    original = original * 2
        #nums = set(nums)
        #while original in nums:
        #    original = original * 2
        a_dict = {num : 0 for num in nums}
        while original in a_dict:
            original = original * 2
        return original