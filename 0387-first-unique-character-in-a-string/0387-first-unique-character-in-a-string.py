class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = dict(Counter(s))
        for idx, c in enumerate(s):
            if cnt[c] == 1:
                return idx
        return -1