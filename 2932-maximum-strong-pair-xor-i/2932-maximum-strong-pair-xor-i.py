class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = -10e4
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    continue
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    ans = max(ans, nums[i] ^ nums[j])      
        return ans if ans != -10e4 else 0