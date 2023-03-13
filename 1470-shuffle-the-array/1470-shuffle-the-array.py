class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = list()
        for p in zip(nums[:n], nums[n:]):
            ans.extend(p)
        return ans