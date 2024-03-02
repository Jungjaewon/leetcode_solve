class Solution:
    def maxDepth(self, s: str) -> int:
        ans,stack = 0, list()
        o_cnt = 0
        for c in s:
            if '(' == c:
                o_cnt += 1
            elif ')' == c:
                ans = max(ans, o_cnt)
                o_cnt -= 1
        return ans