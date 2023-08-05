class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = sqrt(a * a + b * b)
                if c <= n and int(c) == c:
                    ans += 1
        return ans