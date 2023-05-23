class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = list()
        for n, idx in zip(nums,index):
            ans.insert(idx, n)
        return ans