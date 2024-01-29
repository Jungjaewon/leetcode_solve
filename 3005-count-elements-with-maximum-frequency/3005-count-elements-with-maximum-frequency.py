class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a_dict = dict(Counter(nums))
        max_v = max(list(a_dict.values()))
        return sum([ value for key, value in a_dict.items() if value == max_v])