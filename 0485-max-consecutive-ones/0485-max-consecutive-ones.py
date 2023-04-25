class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, temp = 0, 0
        for n in nums:
            if n == 1:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(ans, temp)
        return ans