class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([k for k,v in Counter(nums).items() if v == 1])
        #ans_dict = defaultdict(int)
        #for n in nums:
        #    ans_dict[n] += 1
        #return sum([n for n in ans_dict if ans_dict[n] == 1])