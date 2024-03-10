class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for k in range(1, len(nums) + 1):
            candidate = [ list(x) for x in list(itertools.combinations(nums, k))]
            sub_ans = 0
            for candi in candidate:
                sub_ans += reduce(lambda a, b: a ^ b, candi, 0)
            ans += sub_ans
        return ans