class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        a_set = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in a_set:
                return True
            else:
                a_set.add(s)
        return False