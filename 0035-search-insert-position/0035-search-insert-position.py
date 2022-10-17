class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        
        while s <= e:
            m = (s + e) // 2
            #print(f's : {s}, e : {e}, m : {m}')
            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        #print(f'out s : {s}, e : {e}, m : {m}')
        return s