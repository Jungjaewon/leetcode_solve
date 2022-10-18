class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32, -1, -1):
            if n & 1 << i:
                ans = ans | 1 << 31 - i 
            else:
                pass
        
        return ans
        