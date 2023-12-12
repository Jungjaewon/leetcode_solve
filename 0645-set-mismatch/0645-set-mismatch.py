class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        n_set = set(range(1, len(nums) + 1))
        a_0 = [k for k, v in dict(Counter(nums)).items() if v == 2][0]
        a_1 = list(n_set - set(nums))[0]
        return [a_0, a_1]
        """
        """
        a_0 = [k for k, v in dict(Counter(nums)).items() if v == 2][0]
        a_1 = list(set(range(1, len(nums) + 1)) - set(nums))[0]
        return [a_0, a_1]
        """
        a_0 = [k for k, v in Counter(nums).items() if v == 2][0]
        a_1 = list(set(range(1, len(nums) + 1)) - set(nums))[0]
        return [a_0, a_1]
        