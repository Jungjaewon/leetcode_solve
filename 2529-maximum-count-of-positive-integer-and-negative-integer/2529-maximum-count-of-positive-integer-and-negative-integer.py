class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        #return max(sum([1 for n in nums if n > 0]), sum([1 for n in nums if n < 0]))
        #return max(len([1 for n in nums if n > 0]), len([1 for n in nums if n < 0]))
        #return max(len(list(filter(lambda x : x > 0, nums))), len(list(filter(lambda x : x < 0, nums))))
        return max(sum(list(map(lambda x : 1 if x > 0 else 0, nums))), sum(list(map(lambda x : 1if x < 0 else 0, nums))))