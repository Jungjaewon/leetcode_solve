class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans_set = set()
        for s, e in nums:
            for i in range(s, e + 1):
                ans_set.add(i)
        return len(ans_set)