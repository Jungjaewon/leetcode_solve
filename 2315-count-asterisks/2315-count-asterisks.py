class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(chunk.count('*') for chunk in s.split('|')[0::2])
    # https://leetcode.com/problems/count-asterisks/discuss/3219947/Python-O(n)
    # https://leetcode.com/problems/count-asterisks/discuss/2484633/Python-Elegant-and-Short-or-Two-solutions-or-One-pass-One-line