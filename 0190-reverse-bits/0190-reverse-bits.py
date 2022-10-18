class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            if n & 1 << i:
                ans = ans | 1 << 31 - i         
        return ans
        # return sum(bool(2 ** i & n) * (2 ** j) for i, j in zip(range(32), range(31, -1, -1)))
        """
        out = 0, n = 1101101
        out = 01, n = 110110
        out = 010, n = 11011
        out = 0101, n = 1101
        out = 01011, n = 110
        out = 010110, n = 11
        out = 0101101, n = 1
        out = 01011011, n = 0
        def reverseBits(self, n):
            out = 0
            for i in range(32):
                out = (out << 1)^(n & 1)
                n >>= 1 # n = n >> 1
        return out
        # https://leetcode.com/problems/reverse-bits/discuss/732138/Python-O(32)-simple-solution-explained
        """