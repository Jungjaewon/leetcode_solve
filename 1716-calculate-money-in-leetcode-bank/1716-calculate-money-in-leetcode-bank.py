class Solution:
    def totalMoney(self, n: int) -> int:
        nw, ret, ans = n // 7, n % 7, 0
        cnt = 1
        for i in range(1, nw + 1):
            for j in range(cnt, cnt + 7):
                ans += j
            cnt += 1
        for j in range(cnt, cnt + ret):
            ans += j
        return int(ans)
            