class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = list()
        for i in range(n):
            ans.extend([nums[i], nums[i + n]])
        return ans
        """
        ans = list()
        for p in zip(nums[:n], nums[n:]):
            ans.extend(p)
        return ans
        """
        #return [ x,y for x,y in zip(nums[:n], nums[n:])]