class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans_dict = defaultdict(int)
        for n in nums:
            ans_dict[n] += 1
        return sum([n for n in ans_dict if ans_dict[n] == 1])