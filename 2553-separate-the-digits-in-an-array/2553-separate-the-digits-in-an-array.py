class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [ int(x) for n in nums for x in list(str(n))]