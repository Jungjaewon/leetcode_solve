class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        from itertools import accumulate
        
        left_arr = [0] + nums[0:len(nums) - 1]
        right_arr = nums[1:len(nums)] + [0]
        
        left_arr = list(accumulate(left_arr))
        right_arr = list(accumulate(right_arr[::-1]))[::-1]
        
        ans_arr = list()
        
        return [abs(a - b) for a,b in zip(left_arr, right_arr)]
        