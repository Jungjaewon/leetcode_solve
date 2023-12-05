class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        """
        ans = list()
        for idx in range(1, len(mountain) - 1):
            if mountain[idx - 1] < mountain[idx] and mountain[idx + 1] < mountain[idx]:
                ans.append(idx)
        return ans
        """
        return [ idx for idx in range(1, len(mountain) - 1) if mountain[idx - 1] < mountain[idx] and mountain[idx + 1] < mountain[idx]]