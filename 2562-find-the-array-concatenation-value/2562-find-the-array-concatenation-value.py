class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        """
        ans = 0
        while len(nums):
            if len(nums) == 1:
                ans += nums[0]
                del nums[0]
            else:
                ans += int(str(nums[0]) + str(nums[-1]))
                del nums[0]
                del nums[-1]
        return ans
        """
        ans = 0
        while len(nums):
            if len(nums) == 1:
                ans += nums[0]
                break
            else:
                ans += int(str(nums[0]) + str(nums[-1]))
                nums = nums[1:]
                nums = nums[:-1]
        return ans