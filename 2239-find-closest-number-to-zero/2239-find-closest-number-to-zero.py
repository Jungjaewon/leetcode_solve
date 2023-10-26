class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = list()
        for n in nums:
            ans.append([n, abs(n - 0)])
        ans.sort(key=lambda x : (x[1],-x[0]))
        return ans[0][0]