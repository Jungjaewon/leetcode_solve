class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            matches = n // 2
            teams = n - matches
            n = teams
            ans += matches
        return ans