class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        for idx in range(len(nums)):
            if sum(nums[:idx]) == sum(nums[idx + 1:]):
                return idx
        return -1
        """
        if len(nums) == 1:
            return 0
        left, right = 0, sum(nums[1:])
        if left == right:
            return 0
        else:
            for idx in range(1, len(nums)):
                left += nums[idx - 1]
                right -= nums[idx]
                print(idx, left, right)
                if left == right:
                    return idx
        return -1
        