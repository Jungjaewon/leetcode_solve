class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        len_s = len(columnTitle)
        s_lit = list(columnTitle)
        ans = 0
        for idx, c in enumerate(columnTitle[::-1]):
            ans += (ord(c) - ord('A') + 1) * 26 ** idx
        return ans