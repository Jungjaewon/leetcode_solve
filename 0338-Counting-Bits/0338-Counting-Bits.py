class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        else:
            dp = [0] * (n + 1)
            dp[0], dp[1] = 0, 1
            for i in range(2, len(dp)):
                if i & 1 == 0:
                    dp[i] = dp[i // 2];
                else:
                    dp[i] = dp[i // 2] + 1;
            return dp
