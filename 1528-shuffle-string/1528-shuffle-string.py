class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        ans = ['a'] * len(s)
        for c, index in zip(s,indices):
            ans[index] = c
        return ''.join(ans)
        """
        a_dict = {i : c for c, i in zip(s,indices)}
        return ''.join([a_dict[i] for i in sorted(a_dict.keys())])