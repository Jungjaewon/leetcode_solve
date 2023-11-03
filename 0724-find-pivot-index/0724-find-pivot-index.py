class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for idx in range(len(nums)):
            if idx == 0:
                left_sum = 0
            else:
                left_sum = sum(nums[:idx])
                
            if idx + 1 == len(nums):
                right_sum = 0
            else:
                right_sum = sum(nums[idx + 1 : ])
            
            #print(idx, left_sum, right_sum)
            if left_sum == right_sum:
                return idx
        return -1