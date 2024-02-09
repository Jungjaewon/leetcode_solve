class Solution:
    def maxScore(self, s: str) -> int:
        ans = -10e4
        for i in range(len(s)):
            left_s, right_s = s[:i + 1], s[i + 1:]
            if left_s == "" or right_s == "":
                continue
            ans = max(ans, sum([1 for c in left_s if c == '0'] + [1 for c in right_s if c == '1']))
        return ans