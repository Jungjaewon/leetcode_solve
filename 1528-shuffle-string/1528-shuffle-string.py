class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['a'] * len(s)
        for c, index in zip(s,indices):
            ans[index] = c
        return ''.join(ans)