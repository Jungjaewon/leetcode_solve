class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return [key for key, val in dict(Counter(nums)).items() if val > 1]