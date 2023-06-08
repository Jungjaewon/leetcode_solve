class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        #return max(sum([1 for n in nums if n > 0]), sum([1 for n in nums if n < 0]))
        #return max(len([1 for n in nums if n > 0]), len([1 for n in nums if n < 0]))
        #print(list(filter(lambda x : x > 0, nums)))
        #print(sum(filter(lambda x : x > 0, nums)))
        #print(sum(filter(lambda x : x < 0, nums)))
        return max(len(list(filter(lambda x : x > 0, nums))), len(list(filter(lambda x : x < 0, nums))))