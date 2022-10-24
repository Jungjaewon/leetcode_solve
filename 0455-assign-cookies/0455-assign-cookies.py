from collections import defaultdict
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int: 
        i, j, ans = 0, 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans, i = ans + 1, i + 1
            j += 1
        return ans
    # Reference https://leetcode.com/problems/assign-cookies/discuss/2627736/Python-or-Easy-to-understand-or-Simple
    # Read Carefully