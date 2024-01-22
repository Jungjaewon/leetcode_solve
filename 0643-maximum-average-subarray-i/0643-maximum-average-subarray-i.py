class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        ans = -10e4
        for i in range(len(nums) - k + 1):
            #print(nums[i : i + k])
            ans = max(ans, sum(nums[i : i + k]) / k)
        return ans
        """
        #https://leetcode.com/problems/maximum-average-subarray-i/discuss/4448468/Python3-beat-99-Solution-oror-Easy-Pictures-explanation
        ans= window = sum(nums[:k])
        for i in range(1,len(nums)-k+1):            
            window = window - nums[i-1] + nums[i+k-1]
            ans = max(window, ans)
        return ans/k