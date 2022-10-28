class Solution:
    def findComplement(self, num: int) -> int:
        last_idx, ans = 0, 0
        for i in range(31, -1, -1):
            if num & 1 << i:
                last_idx = i + 1
                break
        
        for i in range(last_idx):
            
            if not (num & 1 << i):
                ans = ans | 1 << i
        return ans
        