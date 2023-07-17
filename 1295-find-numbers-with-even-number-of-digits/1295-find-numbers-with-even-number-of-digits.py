class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #return sum([1 if len(str(x)) % 2 == 0 else 0 for x in nums])
        return len([1 for x in nums if len(str(x)) % 2 == 0 ])