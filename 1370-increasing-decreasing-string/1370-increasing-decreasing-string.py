class Solution:
    def sortString(self, s: str) -> str:
        def key(c, phase={}):
            p = phase[c] = phase.get(c, -1) + 1
            return p, ord(c) * (-1)**p
        return ''.join(sorted(s, key=key))
    #https://leetcode.com/problems/increasing-decreasing-string/discuss/532293/4-lines-Python-sort-by-key
    #https://leetcode.com/problems/increasing-decreasing-string/discuss/531811/JavaPython-3-Two-clean-codes-w-explanation-and-analysis.