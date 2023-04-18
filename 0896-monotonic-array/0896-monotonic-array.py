class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif len(nums) == 2:
            return nums[0] <= nums[1] or nums[0] >= nums[1] 
        else:
            result_1, result_2 = list(), list()
            temp = nums[0]
            for n in nums[1:]:
                if temp <= n:
                    temp = n
                    result_1.append(True)
                else:
                    result_1.append(False)
            temp = nums[0]
            for n in nums[1:]:
                if temp >= n:
                    temp = n
                    result_2.append(True)
                else:
                    result_2.append(False)
            #print(all(result_1), result_1)
            #print(all(result_2), result_2)
            return all(result_1) or all(result_2)
            