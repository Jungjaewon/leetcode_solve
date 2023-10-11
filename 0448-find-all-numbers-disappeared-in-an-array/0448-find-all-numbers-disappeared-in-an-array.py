class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        a_dict = dict()
        for n in range(1, len(nums) + 1):
            a_dict[n] = 0
        for n in nums:
            a_dict[n] += 1
        return [x for x in a_dict if a_dict[x] == 0]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))
            