class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(digit: int):
            cnt = 0
            for i in range(32):
                if digit & 1 << i:
                    cnt += 1
            return cnt
        return [ helper(i) for i in range(n + 1)]