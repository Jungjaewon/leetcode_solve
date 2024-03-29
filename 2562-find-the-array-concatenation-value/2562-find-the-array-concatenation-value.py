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
        """
        """
        ans = 0
        if len(nums) & 1 == 1:
            mid = (len(nums) // 2)
            ans += nums[mid]
            del nums[mid]
        i,j = 0, len(nums) - 1
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i,j = i + 1, j - 1
        return ans
        """
        ans = 0
        if len(nums) & 1 == 1:
            mid = (len(nums) // 2)
            ans += nums[mid]
            del nums[mid]    
        for a,b in list(zip(nums, nums[::-1]))[:len(nums) // 2]:
            ans += int(str(a) + str(b))
        return ans
        
        
        
        
            