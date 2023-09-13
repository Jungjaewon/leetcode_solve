class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans, idx = list(), 0
        
        while idx < len(nums):
            s, t = nums[idx], nums[idx]
            flag = False
            while idx + 1 < len(nums) and t + 1 == nums[idx + 1]:
                t = nums[idx + 1]
                idx += 1
                flag = True
            if flag:
                ans.append(f"{s}->{t}")
            else:
                ans.append(f"{s}")
            idx += 1
        return ans
            
            