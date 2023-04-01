class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for c in jewels:
            ans += len([ 1 for s in stones if c == s])
        return ans
            