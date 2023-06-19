class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a_dict = dict(Counter(nums))
        for _, item in a_dict.items():
            if item % 2 != 0:
                return False
        return True