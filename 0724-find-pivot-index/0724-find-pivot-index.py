class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        for idx in range(len(nums)):
            if idx == 0:
                left_sum = 0
            else:
                left_sum = sum(nums[:idx])
                
            if idx + 1 == len(nums):
                right_sum = 0
            else:
                right_sum = sum(nums[idx + 1 : ])

            if left_sum == right_sum:
                return idx
        return -1
        """
        left_s, right_s = 0, sum(nums[1:])
        
        for idx in range(len(nums)):
            if left_s == right_s:
                return idx
            else:
                left_s += nums[idx]
                if idx + 1 == len(nums):
                    right_s -= nums[idx]
                else:
                    right_s -= nums[idx + 1]
        return -1