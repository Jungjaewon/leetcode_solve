class Solution:
    def maxPower(self, s: str) -> int:
        ans, temp_c, cnt = list(), '', 0
        for c in s:
            if temp_c == '':
                temp_c, cnt = c, 1
            elif temp_c == c:
                cnt += 1
            else:
                ans.append(cnt)
                temp_c, cnt = c, 1
        ans.append(cnt)
        return max(ans)
        