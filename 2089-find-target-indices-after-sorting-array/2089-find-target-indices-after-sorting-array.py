class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        ans = list()
        for i, n in enumerate(sorted(nums)):
            if n == target:
                ans.append(i)
        return ans
        """
        return [i for i, n in enumerate(sorted(nums)) if n == target]