class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        ans = [s[i : i + 3] for i in range(len(s) - 2)]
        return len([x for x in ans if len(x) == len(set(x))])
        """
        return len([x for x in [s[i : i + 3] for i in range(len(s) - 2)] if len(x) == len(set(x))])
        