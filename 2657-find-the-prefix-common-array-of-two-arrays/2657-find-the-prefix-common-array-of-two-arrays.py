class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0] * len(A)
        for i in range(len(ans)):
            ans[i] = len(set(A[:i + 1]).intersection(set(B[:i + 1])))
        return ans