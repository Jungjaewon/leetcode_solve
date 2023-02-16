class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i +1, len(nums)): 
                ans = ans + 1 if (i * j) % k == 0 and nums[i] == nums[j] else ans
        return ans
                    