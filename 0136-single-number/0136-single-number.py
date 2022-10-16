class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans_dict = dict()
        for n in nums:
            if n not in ans_dict:
                ans_dict[n] = 0
            ans_dict[n] += 1
        
        for n in ans_dict:
            if ans_dict[n] == 1:
                return n